#!/usr/bin/env python3
"""
LeetCode-style judge for C++ practice kits.

    python driver.py --list           list the questions in this kit
    python driver.py -1               judge question 1 (stops at the first failure, like Submit)
    python driver.py -1 -s            sample tests only (like the Run button)
    python driver.py -1 --case 7      run test #7 and print its input, output and expected in full
    python driver.py -1 --all         keep going after the first failure
    python driver.py -1 --tl 3        time limit per test in seconds (default 2)
    python driver.py -1 --reset       restore the blank template (your code is saved as solution.cpp.bak)

Layout it expects (nothing to configure):
    q<k>_<slug>/PROBLEM.md            first line "# Q<k>. <Title>"
    q<k>_<slug>/solution.cpp          the file you edit
    q<k>_<slug>/tests/NN.in, NN.out   tests; an empty NN.sample marks a sample
    _mathworks/q<k>_main.cpp            reads stdin, calls Solution, prints (do not edit)
    _mathworks/q<k>_template.cpp        the blank solution.cpp
Set CXX to use another compiler (default g++).
"""
import argparse, os, re, shutil, subprocess, sys, tempfile, time

ROOT = os.path.dirname(os.path.abspath(__file__))
HARNESS = os.path.join(ROOT, "_mathworks")
IS_WIN = os.name == "nt"

if IS_WIN:
    os.system("")  # enables ANSI colours on Windows 10+
USE_COLOR = sys.stdout.isatty() and os.environ.get("NO_COLOR") is None
def c(text, code):
    return f"\033[{code}m{text}\033[0m" if USE_COLOR else text
GREEN, RED, YELLOW, DIM, BOLD, CYAN = "32", "31", "33", "2", "1", "36"
COLOR = {"Accepted": GREEN, "Wrong Answer": RED, "Time Limit Exceeded": YELLOW, "Runtime Error": RED}


def clip(s, limit=1200):
    s = s.rstrip("\n")
    return s if len(s) <= limit else s[:limit] + c(f"\n... ({len(s) - limit} more characters, use --case to see all)", DIM)


def discover():
    qs = {}
    for name in sorted(os.listdir(ROOT)):
        m = re.match(r"^q(\d+)_", name)
        if m and os.path.isdir(os.path.join(ROOT, name)):
            title = name
            pm = os.path.join(ROOT, name, "PROBLEM.md")
            if os.path.exists(pm):
                with open(pm, encoding="utf-8") as f:
                    first = f.readline().strip().lstrip("#").strip()
                title = re.sub(r"^Q\d+\.\s*", "", first) or name
            qs[int(m.group(1))] = (name, title)
    return qs


def load_tests(folder, samples_only):
    tdir = os.path.join(ROOT, folder, "tests")
    tests = []
    for f in sorted(os.listdir(tdir)):
        if f.endswith(".in"):
            name = f[:-3]
            sample = os.path.exists(os.path.join(tdir, name + ".sample"))
            if samples_only and not sample:
                continue
            with open(os.path.join(tdir, f)) as fi, open(os.path.join(tdir, name + ".out")) as fo:
                tests.append((name, sample, fi.read(), fo.read()))
    return tests


def compile_solution(q, folder, workdir):
    cxx = os.environ.get("CXX", "g++")
    if shutil.which(cxx) is None:
        sys.exit(f"Could not find the C++ compiler '{cxx}'. Install g++ (or set CXX) and try again.")
    exe = os.path.join(workdir, "sol.exe" if IS_WIN else "sol")
    cmd = [cxx, "-std=c++17", "-O2", "-I", os.path.join(ROOT, folder),
           os.path.join(HARNESS, f"q{q}_main.cpp"), "-o", exe]
    print(c("Compiling...", DIM), end=" ", flush=True)
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(c("\nCompile Error", RED + ";" + BOLD))
        print(clip(r.stderr or r.stdout, 4000))
        return None
    print(c("ok", DIM))
    return exe


def run_one(exe, inp, tl):
    t0 = time.perf_counter()
    try:
        r = subprocess.run([exe], input=inp, capture_output=True, text=True, timeout=tl)
    except subprocess.TimeoutExpired as e:
        out = e.stdout.decode() if isinstance(e.stdout, bytes) else (e.stdout or "")
        return "Time Limit Exceeded", out, "", tl
    secs = time.perf_counter() - t0
    return ("Runtime Error" if r.returncode != 0 else None), r.stdout, r.stderr, secs


def judge(q, folder, tests, tl, keep_going, show_full):
    workdir = tempfile.mkdtemp(prefix="judge_")
    try:
        exe = compile_solution(q, folder, workdir)
        if exe is None:
            return 1
        passed, fail, worst = 0, None, 0.0
        for name, sample, inp, expected in tests:
            verdict, out, err, secs = run_one(exe, inp, tl)
            if verdict is None:
                verdict = "Accepted" if out.split() == expected.split() else "Wrong Answer"
            worst = max(worst, secs)
            tag = c(f"{'(sample)' if sample else '':<10}", CYAN)
            print(f"  #{name} {tag}{c(f'{verdict:<20}', COLOR[verdict])} {c(f'{secs * 1000:7.0f} ms', DIM)}")
            if verdict == "Accepted":
                passed += 1
                if show_full:
                    print(c("\nInput:", BOLD)); print(inp.rstrip("\n"))
                    print(c("Output:", BOLD)); print(out.rstrip("\n"))
                    print(c("Expected:", BOLD)); print(expected.rstrip("\n"))
            elif fail is None:
                fail = (name, verdict, inp, out, err, expected)
                if not keep_going:
                    break
        print(c("-" * 60, DIM))
        if fail is None:
            print(c(f"Accepted   {passed} / {len(tests)} testcases passed", GREEN + ";" + BOLD)
                  + c(f"   (slowest {worst * 1000:.0f} ms, limit {tl * 1000:.0f} ms)", DIM))
            return 0
        name, verdict, inp, out, err, expected = fail
        lim = 10**9 if show_full else 1200
        print(c(f"{verdict}   {passed} / {len(tests)} testcases passed", COLOR[verdict] + ";" + BOLD))
        print(c(f"\nLast executed input (test #{name}):", BOLD))
        print(clip(inp, lim))
        if verdict == "Time Limit Exceeded":
            print(c(f"\nYour program ran longer than {tl:.1f} s.", YELLOW))
        else:
            print(c("\nOutput:", BOLD))
            print(clip(out, lim) if out.strip() else c("(empty)", DIM))
            print(c("Expected:", BOLD))
            print(clip(expected, lim))
        if err.strip():
            print(c("\nstderr:", BOLD))
            print(clip(err, 3000))
        return 1
    finally:
        shutil.rmtree(workdir, ignore_errors=True)


def main():
    qs = discover()
    ap = argparse.ArgumentParser(description="LeetCode-style C++ judge.",
                                 formatter_class=argparse.RawDescriptionHelpFormatter, epilog=__doc__)
    g = ap.add_mutually_exclusive_group(required=True)
    for k, (_, title) in qs.items():
        g.add_argument(f"-{k}", dest="q", action="store_const", const=k, help=title)
    g.add_argument("--list", action="store_true", help="list the questions")
    ap.add_argument("-s", "--samples", action="store_true", help="run only the sample tests")
    ap.add_argument("-c", "--case", type=int, help="run one test number and print it in full")
    ap.add_argument("-a", "--all", action="store_true", help="keep running after the first failure")
    ap.add_argument("--tl", type=float, default=2.0, help="time limit per test in seconds (default 2)")
    ap.add_argument("--reset", action="store_true", help="restore the blank template")
    args = ap.parse_args()

    if args.list:
        for k, (folder, title) in qs.items():
            print(f"  -{k}  {title}   ({folder}/)")
        return 0

    q = args.q
    folder, title = qs[q]
    sol = os.path.join(ROOT, folder, "solution.cpp")
    if args.reset:
        if os.path.exists(sol):
            shutil.copy(sol, sol + ".bak")
            print(f"Saved your current code to {folder}/solution.cpp.bak")
        shutil.copy(os.path.join(HARNESS, f"q{q}_template.cpp"), sol)
        print(f"Restored the blank template: {folder}/solution.cpp")
        return 0

    tests = load_tests(folder, args.samples)
    if args.case is not None:
        tests = [t for t in load_tests(folder, False) if int(t[0]) == args.case]
        if not tests:
            sys.exit(f"No test #{args.case} for question {q}.")
    print(c(f"Q{q} - {title}", BOLD) + c(f"   [{folder}/solution.cpp]", DIM))
    return judge(q, folder, tests, args.tl, args.all or args.case is not None, args.case is not None)


if __name__ == "__main__":
    sys.exit(main())
