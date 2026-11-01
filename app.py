"""Local DSA judge: Flask server serving the UI and the judge API."""
import json
import re
import sys
import threading
import time
from pathlib import Path

from flask import Flask, abort, jsonify, render_template, request, send_file

import judge

ROOT = Path(__file__).resolve().parent
PROBLEMS_DIR = ROOT / "problems"
SUBMISSIONS_DIR = ROOT / "submissions"
DRAFTS_DIR = ROOT / "drafts"
LOAD_LIMIT_BYTES = 300_000  # larger test inputs are download-only
MAX_INPUT_BYTES = 2_000_000
drafts_lock = threading.Lock()
SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")
LANGS = {"cpp", "python"}
MAX_CODE_BYTES = 200_000

app = Flask(__name__)
# One judge run at a time, so timings aren't skewed by parallel runs.
judge_lock = threading.Lock()


def problem_dir(slug):
    if not SLUG_RE.match(slug or ""):
        abort(404)
    d = PROBLEMS_DIR / slug
    if not (d / "problem.json").exists():
        abort(404)
    return d


def load_meta(d):
    meta = json.loads((d / "problem.json").read_text(encoding="utf-8"))
    meta.setdefault("title", d.name)
    meta.setdefault("difficulty", "Medium")
    meta.setdefault("tags", [])
    meta.setdefault("time_limit_ms", 1000)
    meta.setdefault("memory_mb", 256)
    meta["slug"] = d.name
    return meta


def load_submissions(slug):
    f = SUBMISSIONS_DIR / f"{slug}.json"
    if not f.exists():
        return []
    try:
        return json.loads(f.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []


def save_submission(slug, entry):
    SUBMISSIONS_DIR.mkdir(exist_ok=True)
    subs = load_submissions(slug)
    subs.insert(0, entry)
    (SUBMISSIONS_DIR / f"{slug}.json").write_text(json.dumps(subs[:200], indent=1), encoding="utf-8")


@app.route("/")
def index():
    return render_template("index.html")


@app.get("/api/problems")
def api_problems():
    out = []
    if PROBLEMS_DIR.exists():
        for d in sorted(PROBLEMS_DIR.iterdir()):
            if not (d / "problem.json").exists():
                continue
            meta = load_meta(d)
            subs = load_submissions(d.name)
            meta["status"] = ("solved" if any(s["verdict"] == "AC" for s in subs)
                              else "attempted" if subs else "new")
            meta["tests"] = len(judge.list_tests(d / "tests"))
            out.append({k: meta[k] for k in
                        ("slug", "title", "difficulty", "tags", "status", "tests", "order")
                        if k in meta})
    out.sort(key=lambda m: (m.get("order", 10**9), m["title"].lower()))
    return jsonify(out)


@app.get("/api/problems/<slug>")
def api_problem(slug):
    d = problem_dir(slug)
    meta = load_meta(d)
    statement_file = d / "statement.md"
    meta["statement"] = statement_file.read_text(encoding="utf-8") if statement_file.exists() else ""
    # Only sample tests are ever sent to the browser; the rest stay hidden.
    meta["samples"] = [
        {"input": i.read_text(encoding="utf-8"), "output": o.read_text(encoding="utf-8")}
        for name, i, o in judge.list_tests(d / "tests") if name.startswith("sample")
    ]
    meta["total_tests"] = len(judge.list_tests(d / "tests"))
    meta["python_time_factor"] = judge.PYTHON_TIME_FACTOR
    meta["draft"] = load_draft(slug)
    return jsonify(meta)


def load_draft(slug):
    f = DRAFTS_DIR / f"{slug}.json"
    try:
        return json.loads(f.read_text(encoding="utf-8")) if f.exists() else {}
    except json.JSONDecodeError:
        return {}


@app.post("/api/draft")
def api_draft():
    """Autosave of the editor contents, custom input and language, so a reload restores them."""
    data = request.get_json(force=True, silent=True) or {}
    slug = data.get("slug")
    problem_dir(slug)
    with drafts_lock:
        draft = load_draft(slug)
        for lang, code in (data.get("drafts") or {}).items():
            if lang in LANGS and isinstance(code, str) and len(code.encode("utf-8")) <= MAX_CODE_BYTES:
                draft.setdefault("drafts", {})[lang] = code
        text = data.get("input")
        if isinstance(text, str) and len(text.encode("utf-8")) <= MAX_INPUT_BYTES:
            draft["input"] = text
        if data.get("lang") in LANGS:
            draft["lang"] = data["lang"]
        DRAFTS_DIR.mkdir(exist_ok=True)
        tmp = DRAFTS_DIR / f"{slug}.json.tmp"
        tmp.write_text(json.dumps(draft), encoding="utf-8")
        tmp.replace(DRAFTS_DIR / f"{slug}.json")
    return jsonify(ok=True)


def find_test(slug, name):
    d = problem_dir(slug)
    for n, i, o in judge.list_tests(d / "tests"):
        if n == name:  # looked up in the listing, so no user-supplied path is ever opened
            return i, o
    abort(404)


@app.get("/api/problems/<slug>/tests")
def api_tests(slug):
    d = problem_dir(slug)
    return jsonify([{"name": n, "sample": n.startswith("sample"),
                     "in_bytes": i.stat().st_size, "out_bytes": o.stat().st_size}
                    for n, i, o in judge.list_tests(d / "tests")])


@app.get("/api/problems/<slug>/tests/<name>")
def api_test(slug, name):
    i, o = find_test(slug, name)
    size = i.stat().st_size
    if size > LOAD_LIMIT_BYTES:
        return jsonify(name=name, too_large=True, in_bytes=size)
    return jsonify(name=name, too_large=False, in_bytes=size,
                   input=i.read_text(encoding="utf-8"), expected=o.read_text(encoding="utf-8"))


@app.get("/api/problems/<slug>/tests/<name>/<kind>")
def api_test_file(slug, name, kind):
    if kind not in ("in", "out"):
        abort(404)
    i, o = find_test(slug, name)
    return send_file(i if kind == "in" else o, mimetype="text/plain",
                     as_attachment=True, download_name=f"{name}.{kind}")


@app.get("/api/problems/<slug>/submissions")
def api_submissions(slug):
    problem_dir(slug)
    return jsonify(load_submissions(slug))


def read_code_request():
    data = request.get_json(force=True, silent=True) or {}
    lang, code = data.get("lang"), data.get("code", "")
    if lang not in LANGS:
        abort(400, "Unknown language")
    if not isinstance(code, str) or len(code.encode("utf-8")) > MAX_CODE_BYTES:
        abort(400, "Code too large")
    return data, lang, code


@app.post("/api/submit")
def api_submit():
    data, lang, code = read_code_request()
    slug = data.get("slug")
    d = problem_dir(slug)
    meta = load_meta(d)
    with judge_lock:
        result = judge.judge(lang, code, d / "tests", meta["time_limit_ms"], meta["memory_mb"],
                             meta.get("float_tolerance"))
    entry = {"id": int(time.time() * 1000), "when": time.strftime("%Y-%m-%d %H:%M:%S"),
             "lang": lang, "code": code,
             **{k: result[k] for k in ("verdict", "passed", "total", "time_ms", "memory_mb", "message")}}
    save_submission(slug, entry)
    return jsonify(result)


@app.post("/api/run")
def api_run():
    data, lang, code = read_code_request()
    time_limit_ms, memory_mb = 2000, 512
    slug = data.get("slug")
    if slug and SLUG_RE.match(slug) and (PROBLEMS_DIR / slug / "problem.json").exists():
        meta = load_meta(PROBLEMS_DIR / slug)
        time_limit_ms, memory_mb = meta["time_limit_ms"], meta["memory_mb"]
    with judge_lock:
        result = judge.run_custom(lang, code, data.get("input", ""), time_limit_ms, memory_mb)
    return jsonify(result)


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5000  # optional: python app.py 5001
    print(f"DSA Judge running at http://127.0.0.1:{port}")
    app.run(host="127.0.0.1", port=port, debug=False, threaded=True)
