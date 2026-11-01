"""Compile, run and compare solutions against test files.

Verdicts: AC (Accepted), WA (Wrong Answer), TLE (Time Limit Exceeded),
MLE (Memory Limit Exceeded), RE (Runtime Error), CE (Compile Error).
"""
import os
import shutil
import signal
import subprocess
import sys
import tempfile
import threading
import time
from pathlib import Path

try:
    import psutil
except ImportError:  # memory tracking is optional
    psutil = None

# Python is slower than C++, so it gets a multiple of the problem's time limit.
PYTHON_TIME_FACTOR = 3.0
COMPILE_TIMEOUT_S = 60
MAX_OUTPUT_BYTES = 64 * 1024 * 1024

IS_WINDOWS = os.name == "nt"
IS_MAC = sys.platform == "darwin"
STACK_BYTES = 256 * 1024 * 1024  # big stack so deep recursion behaves like online judges


def find_compiler():
    # On macOS plain "g++" is clang, which lacks <bits/stdc++.h>; prefer Homebrew's real GCC.
    names = [f"g++-{v}" for v in range(16, 10, -1)] if IS_MAC else []
    for name in names + ["g++", "clang++"]:
        path = shutil.which(name)
        if path:
            return path
    return r"C:\msys64\ucrt64\bin\g++.exe" if IS_WINDOWS else "g++"


GPP = find_compiler()
if IS_WINDOWS:
    CPP_FLAGS = ["-O2", "-std=c++17", "-static", "-pipe", f"-Wl,--stack,{STACK_BYTES}"]
elif IS_MAC:
    CPP_FLAGS = ["-O2", "-std=c++17", "-pipe", f"-Wl,-stack_size,{STACK_BYTES:#x}"]
else:
    CPP_FLAGS = ["-O2", "-std=c++17", "-pipe"]  # stack is raised with ulimit at run time

# Common POSIX crash signals, shown in Runtime Error messages.
# (Looked up by name: Windows' signal module lacks SIGKILL and SIGBUS.)
SIGNAL_NAMES = {getattr(signal, name): text for name, text in {
    "SIGSEGV": "Segmentation fault",
    "SIGFPE": "Floating-point exception (e.g. division by zero)",
    "SIGABRT": "Aborted (assert / abort / uncaught exception)",
    "SIGKILL": "Killed (often out of memory)",
    "SIGILL": "Illegal instruction (often undefined behaviour)",
    "SIGBUS": "Bus error (bad memory access)",
}.items() if hasattr(signal, name)}

# Common Windows NTSTATUS crash codes, shown in Runtime Error messages.
WINDOWS_EXIT_CODES = {
    0xC0000005: "Access violation (segmentation fault)",
    0xC00000FD: "Stack overflow",
    0xC0000094: "Integer division by zero",
    0xC000008E: "Floating-point division by zero",
    0xC0000409: "Stack buffer overrun / abort",
    0xC0000017: "Out of memory",
    0xC000001D: "Illegal instruction (often undefined behaviour, e.g. division by zero)",
    0x80000003: "Breakpoint / assertion",
}


if IS_WINDOWS:
    # Child processes inherit the error mode. Without this, a crashing solution sits in
    # Windows Error Reporting until the time limit and shows up as TLE instead of RE.
    import ctypes
    SEM_FAILCRITICALERRORS, SEM_NOGPFAULTERRORBOX, SEM_NOOPENFILEERRORBOX = 0x0001, 0x0002, 0x8000
    ctypes.windll.kernel32.SetErrorMode(
        SEM_FAILCRITICALERRORS | SEM_NOGPFAULTERRORBOX | SEM_NOOPENFILEERRORBOX)


def describe_exit(code):
    if code is None:
        return "killed"
    if code < 0 and not IS_WINDOWS:  # POSIX: killed by signal -code
        try:
            sig = signal.Signals(-code)
        except ValueError:
            return f"killed by signal {-code}"
        return f"{SIGNAL_NAMES.get(sig, sig.name)} ({sig.name})"
    unsigned = code & 0xFFFFFFFF
    if unsigned in WINDOWS_EXIT_CODES:
        return f"{WINDOWS_EXIT_CODES[unsigned]} (exit code 0x{unsigned:08X})"
    if code == 3:
        return "abort() called (exit code 3)"
    return f"exit code {code}"


def kill_tree(proc):
    if IS_WINDOWS:
        subprocess.run(["taskkill", "/T", "/F", "/PID", str(proc.pid)],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        try:  # solutions run in their own session, so this also kills anything they spawned
            os.killpg(proc.pid, signal.SIGKILL)
        except (ProcessLookupError, PermissionError):
            pass


def tail(text, limit=3000):
    text = text or ""
    return text if len(text) <= limit else "...\n" + text[-limit:]


def clip(text, limit=3000):
    text = text or ""
    return text if len(text) <= limit else text[:limit] + f"\n... ({len(text) - limit} more characters)"


class Program:
    """A compiled (or interpretable) solution living in a temp directory."""

    def __init__(self, lang, code):
        self.lang = lang
        self.dir = Path(tempfile.mkdtemp(prefix="judge_"))
        self.cmd = None
        self.compile_error = None
        self._build(code)

    def _build(self, code):
        if self.lang == "cpp":
            src = self.dir / "sol.cpp"
            exe = self.dir / ("sol.exe" if IS_WINDOWS else "sol")
            src.write_text(code, encoding="utf-8")
            try:
                res = subprocess.run([GPP, *CPP_FLAGS, str(src), "-o", str(exe)],
                                     capture_output=True, text=True, timeout=COMPILE_TIMEOUT_S)
            except subprocess.TimeoutExpired:
                self.compile_error = "Compilation timed out"
                return
            except FileNotFoundError:
                self.compile_error = f"g++ not found (looked for {GPP})"
                return
            if res.returncode != 0:
                self.compile_error = tail(res.stderr.replace(str(src), "sol.cpp"), 6000)
                return
            self.cmd = [str(exe)]
        elif self.lang == "python":
            src = self.dir / "sol.py"
            src.write_text(code, encoding="utf-8")
            res = subprocess.run([sys.executable, "-m", "py_compile", str(src)],
                                 capture_output=True, text=True)
            if res.returncode != 0:
                self.compile_error = tail(res.stderr.replace(str(src), "sol.py"), 6000)
                return
            self.cmd = [sys.executable, "-X", "utf8", str(src)]
        else:
            self.compile_error = f"Unsupported language: {self.lang}"

    def time_limit_s(self, time_limit_ms):
        factor = PYTHON_TIME_FACTOR if self.lang == "python" else 1.0
        return time_limit_ms / 1000.0 * factor

    def run(self, input_text, time_limit_s, memory_mb=None):
        """Run once. Returns dict(status, stdout, stderr, time_ms, memory_mb, exit_code)."""
        env = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONDONTWRITEBYTECODE="1")
        in_path = self.dir / "input.txt"
        out_path = self.dir / "output.txt"
        err_path = self.dir / "stderr.txt"
        in_path.write_bytes(input_text.encode("utf-8"))

        peak = {"bytes": 0}
        with open(in_path, "rb") as fin, open(out_path, "wb") as fout, open(err_path, "wb") as ferr:
            start = time.perf_counter()
            if IS_WINDOWS:
                proc = subprocess.Popen(self.cmd, stdin=fin, stdout=fout, stderr=ferr,
                                        cwd=self.dir, env=env)
            else:
                # Raise the stack limit, then exec the solution (same pid, so timing,
                # memory tracking and signals all refer to the solution itself).
                cmd = ["/bin/sh", "-c", f'ulimit -s {STACK_BYTES // 1024} 2>/dev/null; exec "$0" "$@"',
                       *self.cmd]
                proc = subprocess.Popen(cmd, stdin=fin, stdout=fout, stderr=ferr,
                                        cwd=self.dir, env=env, start_new_session=True)
            stop = threading.Event()
            watcher = None
            if psutil is not None:
                watcher = threading.Thread(target=_watch_memory,
                                           args=(proc.pid, peak, stop, memory_mb, proc), daemon=True)
                watcher.start()
            status = "OK"
            try:
                proc.wait(timeout=time_limit_s)
            except subprocess.TimeoutExpired:
                kill_tree(proc)
                proc.wait()
                status = "TLE"
            elapsed = time.perf_counter() - start
            stop.set()
            if watcher:
                watcher.join(timeout=1)

        mem_mb = peak["bytes"] / (1024 * 1024)
        stdout = out_path.read_bytes()[:MAX_OUTPUT_BYTES].decode("utf-8", errors="replace")
        stderr = err_path.read_bytes()[-20000:].decode("utf-8", errors="replace")
        if status == "OK":
            if memory_mb and mem_mb > memory_mb:
                status = "MLE"
            elif proc.returncode != 0:
                status = "RE"
        return {
            "status": status,
            "stdout": stdout,
            "stderr": stderr,
            "time_ms": round(elapsed * 1000),
            "memory_mb": round(mem_mb, 1),
            "exit_code": proc.returncode,
        }

    def cleanup(self):
        shutil.rmtree(self.dir, ignore_errors=True)


def _watch_memory(pid, peak, stop, memory_mb, proc):
    try:
        p = psutil.Process(pid)
    except psutil.Error:
        return
    while not stop.is_set():
        try:
            info = p.memory_info()
            used = getattr(info, "peak_wset", None) or info.rss
            peak["bytes"] = max(peak["bytes"], used)
            if memory_mb and used > memory_mb * 1024 * 1024 * 1.5:
                kill_tree(proc)  # way over the limit: stop before it eats the machine
                return
        except psutil.Error:
            return
        time.sleep(0.005)


def outputs_match(actual, expected, float_tol=None):
    a, e = actual.split(), expected.split()
    if len(a) != len(e):
        return False
    if float_tol is None:
        return a == e
    for x, y in zip(a, e):
        if x == y:
            continue
        try:
            fx, fy = float(x), float(y)
        except ValueError:
            return False
        if abs(fx - fy) > float_tol * max(1.0, abs(fy)):
            return False
    return True


def list_tests(tests_dir):
    """Sorted (name, in_path, out_path) triples; sample tests (sample*) come first."""
    tests_dir = Path(tests_dir)
    ins = [p for p in tests_dir.glob("*.in") if p.with_suffix(".out").exists()]
    ins.sort(key=lambda p: (not p.stem.startswith("sample"), p.stem))
    return [(p.stem, p, p.with_suffix(".out")) for p in ins]


def judge(lang, code, tests_dir, time_limit_ms=1000, memory_mb=256, float_tol=None):
    tests = list_tests(tests_dir)
    result = {"verdict": "AC", "passed": 0, "total": len(tests), "time_ms": 0,
              "memory_mb": 0, "failed_test": None, "message": "", "details": None}
    if not tests:
        result.update(verdict="CE", message="This problem has no test cases yet.")
        return result

    prog = Program(lang, code)
    try:
        if prog.compile_error:
            result.update(verdict="CE", message=prog.compile_error)
            return result
        limit_s = prog.time_limit_s(time_limit_ms)
        for idx, (name, in_path, out_path) in enumerate(tests, 1):
            input_text = in_path.read_text(encoding="utf-8")
            expected = out_path.read_text(encoding="utf-8")
            run = prog.run(input_text, limit_s, memory_mb)
            result["time_ms"] = max(result["time_ms"], run["time_ms"])
            result["memory_mb"] = max(result["memory_mb"], run["memory_mb"])

            verdict = run["status"]
            if verdict == "OK":
                verdict = "AC" if outputs_match(run["stdout"], expected, float_tol) else "WA"
            if verdict == "AC":
                result["passed"] += 1
                continue

            result["verdict"] = verdict
            result["failed_test"] = idx
            if verdict == "TLE":
                result["message"] = f"Exceeded {round(limit_s * 1000)} ms on test {idx}"
            elif verdict == "MLE":
                result["message"] = f"Used {run['memory_mb']} MB (limit {memory_mb} MB) on test {idx}"
            elif verdict == "RE":
                result["message"] = f"{describe_exit(run['exit_code'])} on test {idx}"
            else:
                result["message"] = f"Wrong answer on test {idx}"
            result["details"] = {
                "test_name": name,
                "input": clip(input_text), "expected": clip(expected), "output": clip(run["stdout"]),
                "stderr": tail(run["stderr"], 2000),
            }
            break
        return result
    finally:
        prog.cleanup()


def run_custom(lang, code, input_text, time_limit_ms=1000, memory_mb=256):
    prog = Program(lang, code)
    try:
        if prog.compile_error:
            return {"status": "CE", "stdout": "", "stderr": prog.compile_error,
                    "time_ms": 0, "memory_mb": 0, "exit_code": None}
        run = prog.run(input_text, prog.time_limit_s(time_limit_ms), memory_mb)
        if run["status"] == "RE":
            run["stderr"] = (run["stderr"] + "\n" + describe_exit(run["exit_code"])).strip()
        run["stdout"] = tail(run["stdout"], 20000)
        run["stderr"] = tail(run["stderr"], 5000)
        return run
    finally:
        prog.cleanup()
