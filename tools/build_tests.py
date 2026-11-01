"""Build and verify the test data for one problem.

Usage:  python tools/build_tests.py <slug> [--stress N] [--keep-outputs]

Expects problems/<slug>/_author/ to contain:
  solution.cpp | solution.py   reference solution (required)
  brute.cpp    | brute.py      slow but obviously-correct solution (optional, for stress testing)
  gen.py                       generator (optional):
                                 python gen.py write <tests_dir>   -> writes generated *.in files
                                 python gen.py small <seed>        -> prints one small random input

Steps:
  1. gen.py write  -> generated .in files (hand-written tests/*.in are kept)
  2. reference solution -> .out for every .in
  3. stress: brute vs reference on N small random inputs
  4. judge the reference through the real judge -> must be Accepted
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import judge  # noqa: E402


def find_source(author, stem):
    for ext, lang in ((".cpp", "cpp"), (".py", "python")):
        p = author / f"{stem}{ext}"
        if p.exists():
            return lang, p.read_text(encoding="utf-8")
    return None, None


def compile_or_die(lang, code, what):
    prog = judge.Program(lang, code)
    if prog.compile_error:
        sys.exit(f"{what} failed to compile:\n{prog.compile_error}")
    return prog


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("--stress", type=int, default=300, help="random small cases for brute vs reference")
    ap.add_argument("--keep-outputs", action="store_true", help="don't regenerate existing .out files")
    args = ap.parse_args()

    pdir = ROOT / "problems" / args.slug
    author, tests = pdir / "_author", pdir / "tests"
    meta = json.loads((pdir / "problem.json").read_text(encoding="utf-8"))
    tl_ms, mem = meta.get("time_limit_ms", 1000), meta.get("memory_mb", 256)
    tol = meta.get("float_tolerance")
    tests.mkdir(exist_ok=True)

    gen = author / "gen.py"
    if gen.exists():
        print("[1] generating tests ...")
        subprocess.run([sys.executable, str(gen), "write", str(tests)], check=True, cwd=author)

    ref_lang, ref_code = find_source(author, "solution")
    if not ref_lang:
        sys.exit("missing _author/solution.cpp or solution.py")
    ref = compile_or_die(ref_lang, ref_code, "reference")
    try:
        print("[2] producing expected outputs ...")
        for in_path in sorted(tests.glob("*.in")):
            out_path = in_path.with_suffix(".out")
            if args.keep_outputs and out_path.exists():
                continue
            r = ref.run(in_path.read_text(encoding="utf-8"), 60)
            if r["status"] != "OK":
                sys.exit(f"reference {r['status']} on {in_path.name}: {r['stderr'][-500:]}")
            out_path.write_text(r["stdout"], encoding="utf-8", newline="\n")
            print(f"    {in_path.name:<16} {r['time_ms']:>5} ms")

        brute_lang, brute_code = find_source(author, "brute")
        if brute_lang and gen.exists() and args.stress > 0:
            print(f"[3] stress testing brute vs reference on {args.stress} cases ...")
            brute = compile_or_die(brute_lang, brute_code, "brute")
            try:
                for seed in range(1, args.stress + 1):
                    inp = subprocess.run([sys.executable, str(gen), "small", str(seed)],
                                         capture_output=True, text=True, check=True, cwd=author).stdout
                    a, b = ref.run(inp, 10), brute.run(inp, 10)
                    if a["status"] != "OK" or b["status"] != "OK" or not judge.outputs_match(a["stdout"], b["stdout"], tol):
                        sys.exit(f"MISMATCH on seed {seed}\ninput:\n{inp}\nref:\n{a['stdout']}\nbrute:\n{b['stdout']}")
            finally:
                brute.cleanup()
            print("    all agree")
    finally:
        ref.cleanup()

    print("[4] judging reference solution ...")
    res = judge.judge(ref_lang, ref_code, tests, tl_ms, mem, tol)
    print(f"    {res['verdict']}  {res['passed']}/{res['total']}  max {res['time_ms']} ms / limit {tl_ms} ms  "
          f"{res['memory_mb']} MB  {res['message']}")
    if res["verdict"] != "AC":
        sys.exit(1)
    if res["time_ms"] > tl_ms * 0.5:
        print("    WARNING: reference uses over half the time limit; consider raising time_limit_ms")


if __name__ == "__main__":
    main()
