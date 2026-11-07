"use strict";

const TEMPLATES = {
  cpp: `#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    return 0;
}
`,
  python: `import sys
input = sys.stdin.readline

def main():
    pass

main()
`,
};
const VERDICT_NAMES = {
  AC: "Accepted", WA: "Wrong Answer", TLE: "Time Limit Exceeded",
  MLE: "Memory Limit Exceeded", RE: "Runtime Error", CE: "Compile Error",
};
const LOAD_LIMIT_BYTES = 300000;

const $ = (id) => document.getElementById(id);
const state = {
  problems: [], current: null, editor: null, lang: loadPref("lang", "cpp"),
  drafts: {},         // code per language for the open problem (server copy + local edits)
  loadedCase: null,   // a test loaded into Custom input, so Run can show its expected output
  suppress: false,    // true while the code sets the editor text itself (not a user edit)
  pending: null, subs: [],
};

function loadPref(key, fallback) {
  try { return localStorage.getItem("dsa:" + key) ?? fallback; } catch { return fallback; }
}
function savePref(key, value) {
  try { localStorage.setItem("dsa:" + key, value); } catch { /* storage unavailable */ }
}
function escapeHtml(s) {
  return String(s).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
}
function fmtBytes(n) {
  return n < 1024 ? `${n} B` : n < 1048576 ? `${(n / 1024).toFixed(1)} KB` : `${(n / 1048576).toFixed(1)} MB`;
}

async function api(path, body) {
  const opts = body ? { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(body) } : {};
  const res = await fetch(path, opts);
  if (!res.ok) throw new Error(`${res.status} ${res.statusText}`);
  return res.json();
}

/* ---------- Draft autosave (survives reload, and a different address like localhost vs 127.0.0.1) ---------- */
let draftTimer = null;
function queueDraft(part) {
  if (!state.current) return;
  const slug = state.current.slug;
  const p = state.pending && state.pending.slug === slug ? state.pending : { slug, drafts: {} };
  if (part.drafts) Object.assign(p.drafts, part.drafts);
  if (part.input !== undefined) p.input = part.input;
  if (part.lang !== undefined) p.lang = part.lang;
  state.pending = p;
  clearTimeout(draftTimer);
  draftTimer = setTimeout(flushDraft, 400);
}
function flushDraft() {
  clearTimeout(draftTimer);
  const p = state.pending;
  if (!p) return;
  state.pending = null;
  // keepalive lets the request finish even while the tab is closing or reloading
  fetch("/api/draft", { method: "POST", headers: { "Content-Type": "application/json" },
                        body: JSON.stringify(p), keepalive: true }).catch(() => {});
}
window.addEventListener("pagehide", flushDraft);
document.addEventListener("visibilitychange", () => { if (document.hidden) flushDraft(); });

/* ---------- Markdown + math ---------- */
function renderMarkdown(md) {
  // Pull math out first so marked doesn't turn a_i into <em>.
  const maths = [];
  const stash = (tex, display) => { maths.push({ tex, display }); return `@@MATH${maths.length - 1}@@`; };
  md = md.replace(/\$\$([\s\S]+?)\$\$/g, (_, t) => stash(t, true))
         .replace(/\$([^\$\n]+?)\$/g, (_, t) => stash(t, false));
  let html = window.marked ? marked.parse(md) : `<pre>${escapeHtml(md)}</pre>`;
  return html.replace(/@@MATH(\d+)@@/g, (_, i) => {
    const { tex, display } = maths[+i];
    if (!window.katex) return escapeHtml(tex);
    try { return katex.renderToString(tex, { displayMode: display, throwOnError: false }); }
    catch { return escapeHtml(tex); }
  });
}

/* ---------- Editor ---------- */
function codeKey() { return `code:${state.current?.slug}:${state.lang}`; }
function getCode() { return state.editor ? state.editor.getValue() : ""; }
function setCode(code) {
  state.suppress = true;
  try { state.editor.setValue(code); } finally { state.suppress = false; }
}
function persistCode() {
  if (!state.current) return;
  const code = getCode();
  state.drafts[state.lang] = code;
  savePref(codeKey(), code);
  queueDraft({ drafts: { [state.lang]: code } });
}
function loadCode() {
  setCode(state.drafts[state.lang] ?? loadPref(codeKey(), TEMPLATES[state.lang]));
}

function initEditor() {
  return new Promise((resolve) => {
    const fallback = () => {
      const ta = document.createElement("textarea");
      ta.className = "fallback";
      ta.spellcheck = false;
      $("editor").appendChild(ta);
      ta.addEventListener("keydown", (e) => {
        if (e.key === "Tab") { e.preventDefault(); document.execCommand("insertText", false, "    "); }
      });
      state.editor = {
        getValue: () => ta.value, setValue: (v) => { ta.value = v; },
        onChange: (fn) => ta.addEventListener("input", fn), setLanguage: () => {},
      };
      resolve();
    };
    if (!window.require) return fallback();
    require.config({ paths: { vs: "https://cdn.jsdelivr.net/npm/monaco-editor@0.45.0/min/vs" } });
    require(["vs/editor/editor.main"], () => {
      const ed = monaco.editor.create($("editor"), {
        value: "", language: state.lang, theme: "vs-dark", automaticLayout: true,
        fontSize: 14, minimap: { enabled: false }, tabSize: 4, scrollBeyondLastLine: false,
        fontFamily: "Cascadia Code, Consolas, monospace",
      });
      ed.addCommand(monaco.KeyMod.CtrlCmd | monaco.KeyCode.Enter, submit);
      ed.addCommand(monaco.KeyMod.CtrlCmd | monaco.KeyCode.Quote, run);
      state.editor = {
        getValue: () => ed.getValue(), setValue: (v) => ed.setValue(v),
        onChange: (fn) => ed.onDidChangeModelContent(fn),
        setLanguage: (l) => monaco.editor.setModelLanguage(ed.getModel(), l),
      };
      resolve();
    }, fallback);
  });
}

/* ---------- List view ---------- */
async function showList() {
  flushDraft();
  $("problem-view").classList.add("hidden");
  $("list-view").classList.remove("hidden");
  $("crumb").textContent = "";
  document.title = "DSA Judge";
  state.current = null;
  state.problems = await api("/api/problems");
  populateCompanyFilter();
  renderList();
}

function populateCompanyFilter() {
  const sel = $("company-filter");
  if (!sel) return;
  const cur = sel.value;
  const companies = [...new Set(state.problems.flatMap((p) => p.companies || []))].sort();
  sel.innerHTML = `<option value="">All companies</option>` +
    companies.map((c) => `<option value="${escapeHtml(c)}">${escapeHtml(c)}</option>`).join("");
  if (companies.includes(cur)) sel.value = cur;
}

function renderCompanies(list) {
  if (!list || !list.length) return '<span class="muted">—</span>';
  return list.map((c) => `<span class="company-tag">${escapeHtml(c)}</span>`).join("");
}

function renderList() {
  const q = $("search").value.trim().toLowerCase();
  const comp = $("company-filter") ? $("company-filter").value : "";
  const diff = $("diff-filter").value, status = $("status-filter").value;
  const rows = state.problems.filter((p) => {
    const comps = p.companies || [];
    const matchesQuery = !q || p.title.toLowerCase().includes(q) || comps.some((c) => c.toLowerCase().includes(q));
    return (!comp || comps.includes(comp)) && (!diff || p.difficulty === diff) &&
           (!status || p.status === status) && matchesQuery;
  });
  $("empty-list").classList.toggle("hidden", state.problems.length > 0);
  $("problem-rows").innerHTML = rows.map((p) => `
    <tr data-slug="${escapeHtml(p.slug)}">
      <td class="status-dot status-${p.status}">${p.status === "solved" ? "✔" : p.status === "attempted" ? "●" : ""}</td>
      <td>${escapeHtml(p.title)}</td>
      <td>${renderCompanies(p.companies)}</td>
      <td class="diff-${escapeHtml(p.difficulty)}">${escapeHtml(p.difficulty)}</td>
      <td class="muted">${p.tests}</td>
    </tr>`).join("");
}

/* ---------- Problem view ---------- */
async function showProblem(slug) {
  flushDraft();
  $("list-view").classList.add("hidden");
  $("problem-view").classList.remove("hidden");
  const p = await api(`/api/problems/${encodeURIComponent(slug)}`);
  state.current = p;
  state.loadedCase = null;
  state.drafts = { ...(p.draft?.drafts || {}) };
  if (p.draft?.lang) state.lang = p.draft.lang;
  document.title = `${p.title} · DSA Judge`;
  $("crumb").textContent = "/ " + p.title;
  $("p-title").textContent = p.title;
  const pyMs = Math.round(p.time_limit_ms * p.python_time_factor);
  const compBadges = (p.companies || []).map((c) => `<span class="company-tag">${escapeHtml(c)}</span>`).join("");
  $("p-meta").innerHTML = `
    <span class="diff-${escapeHtml(p.difficulty)}">${escapeHtml(p.difficulty)}</span>
    ${compBadges ? `<span>${compBadges}</span>` : ""}
    <span>⏱ ${p.time_limit_ms} ms (Python ${pyMs} ms)</span>
    <span>💾 ${p.memory_mb} MB</span>
    <span>🧪 ${p.total_tests} tests</span>`;
  $("p-statement").innerHTML = renderMarkdown(p.statement);
  $("p-samples").innerHTML = p.samples.length ? "<h3>Examples</h3>" + p.samples.map((s, i) => `
    <div class="sample">
      <div><h4>Input ${i + 1} <button class="copy ghost" data-copy="${i}">copy</button></h4><pre>${escapeHtml(s.input)}</pre></div>
      <div><h4>Output ${i + 1}</h4><pre>${escapeHtml(s.output)}</pre></div>
    </div>`).join("") : "";
  $("custom-input").value = p.draft?.input ?? loadPref(`input:${slug}`, p.samples[0]?.input ?? "");
  $("lang").value = state.lang;
  state.editor.setLanguage(state.lang);
  loadCode();
  setRunOutput("Run your code to see output.", "muted");
  $("verdict-box").innerHTML = '<span class="muted">Submit to judge against all tests.</span>';
  switchTab("statement");
  switchCtab("input");
  loadSubmissions();
  loadTests();
}

function switchTab(name) {
  document.querySelectorAll(".tab").forEach((b) => b.classList.toggle("active", b.dataset.tab === name));
  ["statement", "tests", "submissions"].forEach((n) => $(`tab-${n}`).classList.toggle("hidden", n !== name));
}
function switchCtab(name) {
  document.querySelectorAll(".ctab").forEach((b) => b.classList.toggle("active", b.dataset.ctab === name));
  ["input", "output", "verdict"].forEach((n) => $(`ctab-${n}`).classList.toggle("hidden", n !== name));
}

async function loadSubmissions() {
  const slug = state.current.slug;
  const subs = await api(`/api/problems/${encodeURIComponent(slug)}/submissions`);
  if (state.current?.slug !== slug) return;
  state.subs = subs;
  $("sub-rows").innerHTML = subs.length ? subs.map((s, i) => `
    <tr>
      <td class="muted">${escapeHtml(s.when)}</td>
      <td>${s.lang === "cpp" ? "C++" : "Python"}</td>
      <td class="badge v-${s.verdict}" title="${escapeHtml(s.message || "")}">${VERDICT_NAMES[s.verdict] || s.verdict}</td>
      <td>${s.passed}/${s.total}</td>
      <td class="muted">${s.time_ms} ms</td>
      <td><button class="ghost" data-load="${i}">Load code</button></td>
    </tr>`).join("") : '<tr><td colspan="6" class="muted">No submissions yet.</td></tr>';
}

async function loadTests() {
  const slug = state.current.slug;
  const tests = await api(`/api/problems/${encodeURIComponent(slug)}/tests`);
  if (state.current?.slug !== slug) return;
  const base = `/api/problems/${encodeURIComponent(slug)}/tests`;
  $("test-rows").innerHTML = tests.map((t) => `
    <tr>
      <td>${escapeHtml(t.name)}${t.sample ? ' <span class="muted">(sample)</span>' : ""}</td>
      <td class="muted">${fmtBytes(t.in_bytes)}</td>
      <td>
        ${t.in_bytes <= LOAD_LIMIT_BYTES ? `<button class="ghost" data-load-test="${escapeHtml(t.name)}">Load as input</button>` : ""}
        <a href="${base}/${encodeURIComponent(t.name)}/in">.in</a>
        <a href="${base}/${encodeURIComponent(t.name)}/out">.out</a>
      </td>
    </tr>`).join("");
}

async function loadTestIntoInput(name) {
  const t = await api(`/api/problems/${encodeURIComponent(state.current.slug)}/tests/${encodeURIComponent(name)}`);
  if (t.too_large) {
    alert(`Test ${name} is ${fmtBytes(t.in_bytes)}, too big for the input box. Use the .in download and run it from a terminal.`);
    return;
  }
  $("custom-input").value = t.input;
  state.loadedCase = { input: t.input, output: t.expected };
  queueDraft({ input: t.input });
  switchCtab("input");
}

function setBusy(busy) {
  $("run-btn").disabled = busy;
  $("submit-btn").disabled = busy;
}

function setRunOutput(text, cls) {
  const out = $("run-output");
  out.className = `plain ${cls || ""}`;
  out.textContent = text;
}

async function run() {
  if (!state.current || $("run-btn").disabled) return;
  setBusy(true);
  switchCtab("output");
  $("run-output").className = "plain muted";
  $("run-output").innerHTML = '<span class="spinner"></span> Running…';
  try {
    const input = $("custom-input").value;
    const r = await api("/api/run", { slug: state.current.slug, lang: state.lang, code: getCode(), input });
    const known = [...state.current.samples, state.loadedCase].filter(Boolean)
      .find((s) => s.input.trim() === input.trim());
    if (r.status === "CE") {
      setRunOutput("Compile Error\n\n" + r.stderr, "v-CE");
    } else if (r.status === "OK" && known) {
      // Running a known test input: compare against its expected output.
      const normLines = (s) => s.split(/\r?\n/).map((l) => l.trim().split(/\s+/).filter(Boolean).join(" ")).filter(Boolean);
      const eLines = normLines(known.output);
      const aLines = normLines(r.stdout);
      const multiTokenLines = eLines.length > 1 && eLines.some((l) => l.includes(" "));
      const ok = multiTokenLines
        ? JSON.stringify(aLines) === JSON.stringify(eLines)
        : aLines.join(" ") === eLines.join(" ");
      const out = $("run-output");
      out.className = "";
      out.innerHTML = `<div class="verdict ${ok ? "v-AC" : "v-WA"}">${ok ? "Passed" : "Wrong Answer"}</div>` +
        `<div class="verdict-stats">${r.time_ms} ms · ${r.memory_mb} MB</div>` +
        `<div class="muted">Expected</div><pre>${escapeHtml(known.output)}</pre>` +
        `<div class="muted">Your output</div><pre>${escapeHtml(r.stdout || "(no output)")}</pre>` +
        (r.stderr ? `<div class="muted">stderr</div><pre>${escapeHtml(r.stderr)}</pre>` : "");
    } else {
      const head = { OK: "Finished", TLE: "Time Limit Exceeded", RE: "Runtime Error", MLE: "Memory Limit Exceeded" }[r.status];
      let text = `${head} · ${r.time_ms} ms · ${r.memory_mb} MB\n\n${r.stdout || "(no output)"}`;
      if (r.stderr) text += `\n\n--- stderr ---\n${r.stderr}`;
      setRunOutput(text, r.status === "OK" ? "" : `v-${r.status}`);
    }
  } catch (e) {
    setRunOutput("Error: " + e.message, "v-RE");
  } finally { setBusy(false); }
}

async function submit() {
  if (!state.current || $("submit-btn").disabled) return;
  setBusy(true);
  switchCtab("verdict");
  $("verdict-box").innerHTML = `<span class="spinner"></span> Judging on ${state.current.total_tests} tests…`;
  try {
    const r = await api("/api/submit", { slug: state.current.slug, lang: state.lang, code: getCode() });
    let html = `<div class="verdict v-${r.verdict}">${VERDICT_NAMES[r.verdict]}</div>`;
    if (r.verdict !== "CE") {
      html += `<div class="verdict-stats">${r.passed}/${r.total} tests passed · max ${r.time_ms} ms · ${r.memory_mb} MB</div>`;
    }
    if (r.message) html += `<pre>${escapeHtml(r.message)}</pre>`;
    const d = r.details;
    if (d) {
      const base = `/api/problems/${encodeURIComponent(state.current.slug)}/tests/${encodeURIComponent(d.test_name)}`;
      html += `<div class="muted">Failed test: <b>${escapeHtml(d.test_name)}</b>
        <button class="ghost" data-load-test="${escapeHtml(d.test_name)}">Load as input</button>
        <a href="${base}/in">.in</a> <a href="${base}/out">.out</a></div>
        <div class="muted">Input</div><pre>${escapeHtml(d.input)}</pre>
        <div class="muted">Expected</div><pre>${escapeHtml(d.expected)}</pre>
        <div class="muted">Your output</div><pre>${escapeHtml(d.output || "(empty)")}</pre>`;
      if (d.stderr) html += `<div class="muted">stderr</div><pre>${escapeHtml(d.stderr)}</pre>`;
    }
    $("verdict-box").innerHTML = html;
    loadSubmissions();
  } catch (e) {
    $("verdict-box").textContent = "Error: " + e.message;
  } finally { setBusy(false); }
}

/* ---------- Wiring ---------- */
function route() {
  const m = location.hash.match(/^#\/p\/([a-z0-9-]+)/);
  (m ? showProblem(m[1]) : showList()).catch((e) => {
    alert("Could not load: " + e.message);
    location.hash = "#/";
  });
}

// Generic drag handle: calls onMove(pointerEvent) while the mouse is held down.
function dragHandle(el, axis, onMove, onDone) {
  el.addEventListener("mousedown", (e) => {
    e.preventDefault();
    el.classList.add("dragging");
    document.body.classList.add("resizing", axis);
    const move = (ev) => onMove(ev);
    const up = () => {
      document.removeEventListener("mousemove", move);
      document.removeEventListener("mouseup", up);
      el.classList.remove("dragging");
      document.body.classList.remove("resizing", axis);
      onDone && onDone();
    };
    document.addEventListener("mousemove", move);
    document.addEventListener("mouseup", up);
  });
}

function initResizers() {
  const left = document.querySelector(".left"), right = document.querySelector(".right");
  const con = $("console");
  const savedW = parseInt(loadPref("leftW", ""), 10);
  if (savedW) left.style.width = savedW + "px";
  const savedH = parseInt(loadPref("consoleH", ""), 10);
  if (savedH) con.style.height = savedH + "px";

  dragHandle($("gutter"), "col", (ev) => {
    left.style.width = Math.max(260, Math.min(ev.clientX, window.innerWidth - 340)) + "px";
  }, () => savePref("leftW", parseInt(left.style.width, 10)));

  dragHandle($("hgutter"), "row", (ev) => {
    const r = right.getBoundingClientRect();
    const h = r.bottom - ev.clientY - 6;  // distance from the pointer to the panel bottom
    con.style.height = Math.max(80, Math.min(h, r.height - 150)) + "px";
  }, () => savePref("consoleH", parseInt(con.style.height, 10)));
}

async function main() {
  ["search", "company-filter", "diff-filter", "status-filter"].forEach((id) => $(id).addEventListener("input", renderList));
  $("problem-rows").addEventListener("click", (e) => {
    const tr = e.target.closest("tr[data-slug]");
    if (tr) location.hash = `#/p/${tr.dataset.slug}`;
  });
  document.querySelectorAll(".tab").forEach((b) => b.addEventListener("click", () => switchTab(b.dataset.tab)));
  document.querySelectorAll(".ctab").forEach((b) => b.addEventListener("click", () => switchCtab(b.dataset.ctab)));
  $("p-samples").addEventListener("click", (e) => {
    const i = e.target.dataset.copy;
    if (i !== undefined) {
      const s = state.current.samples[+i];
      $("custom-input").value = s.input;
      queueDraft({ input: s.input });
      switchCtab("input");
    }
  });
  // "Load as input" buttons appear in the Tests tab and in the verdict box.
  document.addEventListener("click", (e) => {
    const name = e.target.dataset?.loadTest;
    if (name) loadTestIntoInput(name).catch((err) => alert("Could not load test: " + err.message));
  });
  $("sub-rows").addEventListener("click", (e) => {
    const i = e.target.dataset.load;
    if (i === undefined) return;
    const s = state.subs[+i];
    state.lang = s.lang; $("lang").value = s.lang; state.editor.setLanguage(s.lang);
    setCode(s.code);
    persistCode();
    queueDraft({ lang: s.lang });
    savePref("lang", s.lang);
  });
  $("lang").addEventListener("change", () => {
    state.lang = $("lang").value; savePref("lang", state.lang);
    queueDraft({ lang: state.lang });
    state.editor.setLanguage(state.lang);
    loadCode();
  });
  $("reset-btn").addEventListener("click", () => {
    if (!confirm("Replace your code with the starter template?")) return;
    setCode(TEMPLATES[state.lang]);
    persistCode();
  });
  $("custom-input").addEventListener("input", () => {
    if (!state.current) return;
    const v = $("custom-input").value;
    savePref(`input:${state.current.slug}`, v);
    queueDraft({ input: v });
  });
  $("run-btn").addEventListener("click", run);
  $("submit-btn").addEventListener("click", submit);
  initResizers();

  await initEditor();
  state.editor.onChange(() => { if (!state.suppress) persistCode(); });
  window.addEventListener("hashchange", route);
  route();
}

main();
