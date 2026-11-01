# DSA Judge

A practice judge that runs on your own computer. Solve DSA problems in C++17 or Python 3 in a browser
editor and get a verdict against the test cases: Accepted, Wrong Answer, Time Limit Exceeded,
Memory Limit Exceeded, Runtime Error or Compile Error.

## Setup (once)

You need **Git**, **Python 3.10+** and a **C++ compiler**.

| | Windows | macOS | Linux (Ubuntu/Debian) |
|---|---|---|---|
| Git | https://git-scm.com/download/win | `xcode-select --install` | `sudo apt install git` |
| Python | https://www.python.org/downloads/ (tick "Add python.exe to PATH") | `brew install python` | `sudo apt install python3 python3-pip` |
| C++ | Install [MSYS2](https://www.msys2.org/), run `pacman -S mingw-w64-ucrt-x86_64-gcc` in the MSYS2 UCRT64 terminal, then add `C:\msys64\ucrt64\bin` to your PATH | `brew install gcc` (Apple's built-in compiler has no `<bits/stdc++.h>`) | `sudo apt install g++` |

Check that `g++ --version` and `python --version` (or `python3 --version`) work in a new terminal.

Then download the judge:

```
git clone <repo-url>
cd <repo-folder>
```

## Run

- **Windows:** double-click `run.bat`
- **Mac / Linux:** `sh run.sh`

Then open http://127.0.0.1:5000. Ctrl+Enter submits; Ctrl+' runs on your custom input.
Use `python app.py 5001` to run on another port.

## Get new problems

- **Windows:** double-click `update.bat`
- **Mac / Linux:** `sh update.sh`

Then refresh the page. Your saved code and submission history are kept: they live in `drafts/` and
`submissions/`, which Git never touches.

## Using it

- Your code, language and custom input are autosaved, so reloading restores them.
- **Run** on a sample (or a test loaded from the Tests tab) shows the expected output next to yours.
- A failed **Submit** shows the failing test's input, expected output and your output. Long data is cut;
  the `.in`/`.out` links give the full files.
- Python gets 3x the time limit. C++ is compiled with `-O2 -std=c++17` and a 256 MB stack.
- The memory limit is measured by sampling, so treat it as approximate.
- Your code runs directly on your machine with no sandbox, which is fine for your own solutions.

## Adding problems (maintainer)

```
problems/<slug>/
  problem.json   {"title", "difficulty": Easy|Medium|Hard, "time_limit_ms", "memory_mb",
                  "order" (optional), "float_tolerance" (optional, relative)}
  statement.md   Markdown with $math$ (KaTeX). Samples are shown automatically from tests/sample*.
  tests/         sample1.in/.out ... plus any other *.in/*.out
  _author/       solution.cpp|py (reference), brute.cpp|py, gen.py  (kept out of Git)
```

Build and verify tests with `python tools/build_tests.py <slug>`. It generates inputs, writes expected
outputs from the reference solution, stress-tests brute vs reference, then judges the reference (it must
get Accepted). Then commit `problems/<slug>` and push.
