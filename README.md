# DSA Judge

A practice judge that runs on your own computer. Pick a problem, write your solution in **C++** or
**Python** in the browser, and get a verdict against the test cases, just like an online judge:

| Verdict | Meaning |
|---|---|
| **Accepted** | Correct on every test |
| **Wrong Answer** | Your output didn't match on some test |
| **Time Limit Exceeded** | Too slow |
| **Memory Limit Exceeded** | Used too much memory |
| **Runtime Error** | Crashed (segfault, division by zero, exception, ...) |
| **Compile Error** | The code didn't compile |

Nothing is uploaded anywhere: the judge and your code stay on your machine.

---

## Step 1: Install the tools (one time only)

You need three things: **Git**, **Python 3.10 or newer** and a **C++ compiler (g++)**.
Follow the section for your operating system.

### Windows

1. **Git:** download from https://git-scm.com/download/win and install with the default options.
2. **Python:** download from https://www.python.org/downloads/ and run the installer.
   **On the first screen, tick "Add python.exe to PATH"** before clicking Install.
3. **C++ compiler (g++):**
   1. Download and install **MSYS2** from https://www.msys2.org/ (keep the default folder `C:\msys64`).
   2. From the Start menu, open **"MSYS2 UCRT64"** and run:
      ```
      pacman -S mingw-w64-ucrt-x86_64-gcc
      ```
      Press **Enter**, then **Y** when asked.
   3. Add g++ to your PATH: Start menu → search **"Edit the system environment variables"** →
      **Environment Variables...** → under *User variables* select **Path** → **Edit** → **New** →
      type `C:\msys64\ucrt64\bin` → **OK** on every window.
4. **Check:** open a **new** Command Prompt or PowerShell window and run:
   ```
   git --version
   python --version
   g++ --version
   ```
   Each one should print a version number. If not, see [Troubleshooting](#troubleshooting).

### macOS

1. Open **Terminal** and install Apple's developer tools (this includes Git):
   ```
   xcode-select --install
   ```
2. Install **Homebrew** if you don't have it (instructions at https://brew.sh), then:
   ```
   brew install python gcc
   ```
   (Real GCC is needed: Apple's built-in compiler has no `<bits/stdc++.h>`.)
3. **Check:**
   ```
   git --version
   python3 --version
   ls $(brew --prefix)/bin/g++-*
   ```

### Linux (Ubuntu / Debian)

1. Install everything with one command:
   ```
   sudo apt update
   sudo apt install git python3 python3-venv g++
   ```
2. **Check:**
   ```
   git --version
   python3 --version
   g++ --version
   ```

---

## Step 2: Download the judge (one time only)

Open a terminal (Windows: Command Prompt or PowerShell) in the folder where you want the project,
for example your Desktop, and run:

```
git clone https://github.com/manohar135/Dsa-Judge.git
```

This creates a folder called **`Dsa-Judge`**.

---

## Step 3: Start the judge

- **Windows:** open the `Dsa-Judge` folder and **double-click `run.bat`**.
- **macOS / Linux:** in a terminal, run:
  ```
  cd Dsa-Judge
  sh run.sh
  ```

The first start takes a minute while it installs two small Python packages (Flask and psutil).
After that it starts in a few seconds.

Leave that window open while you practise; closing it (or pressing **Ctrl+C**) stops the judge.

---

## Step 4: Open it in your browser

Go to **http://127.0.0.1:5000** (on Windows it opens by itself).

1. Click a problem in the list.
2. Read the statement on the left, choose **C++17** or **Python 3** at the top right, and write your code.
3. Click **Run** to test on the input in the *Custom input* box. It starts with sample 1, and for samples
   it shows the expected output next to yours.
4. Click **Submit** to judge against all test cases.

Shortcuts: **Ctrl+Enter** submits, **Ctrl+'** runs.

Your code, language and custom input are saved automatically, so you can close the browser and come back later.

If a submission fails, the **Verdict** tab shows the failing test's input, the expected output and your output.
The **Tests** tab lists every test case; **Load as input** puts one into *Custom input* so you can debug it.

---

## Step 5: Get new problems

When new problems are added:

- **Windows:** double-click **`update.bat`**
- **macOS / Linux:** `sh update.sh`

Then refresh the browser page. Your saved code and submission history are kept.

---

## How your code is run

- Input comes from **standard input** and output goes to **standard output**, like Codeforces or CodeChef.
  Don't print extra text such as "Enter n:".
- **C++** is compiled with `g++ -O2 -std=c++17` with a 256 MB stack, so deep recursion is fine.
- **Python** gets **3× the time limit** shown on the problem.
- The memory limit is measured approximately.
- Your code runs directly on your computer without a sandbox, which is fine for your own solutions.

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `python` is not recognized, or the Microsoft Store opens | Reinstall Python from python.org and tick **"Add python.exe to PATH"**. Also turn off the Store shortcut: Settings → Apps → Advanced app settings → **App execution aliases** → switch off *python.exe* and *python3.exe*. |
| `g++` is not recognized | Redo the PATH step in Step 1, then open a **new** terminal window. |
| Every C++ submission says *Compile Error: g++ not found* | Same as above: g++ isn't installed or isn't on PATH. |
| `bits/stdc++.h` file not found (macOS) | Run `brew install gcc`. The judge picks up Homebrew's `g++-15` (or similar) automatically. |
| *Could not create a virtual environment* (Linux) | `sudo apt install python3-venv`, then run `sh run.sh` again. |
| *Address already in use* / port 5000 busy | The judge is already running in another window: just open http://127.0.0.1:5000. Or start it on another port: `python app.py 5001` (macOS/Linux: `sh run.sh 5001`) and open http://127.0.0.1:5001. |
| macOS: port 5000 is taken by *AirPlay Receiver* | Use another port as above, or turn off System Settings → General → AirDrop & Handoff → **AirPlay Receiver**. |
| `update.bat` says *Your local changes would be overwritten* | You edited a file that came with the project. Run `git checkout -- .` in the folder to undo those edits (your saved code is **not** affected), then update again. |
| The page looks old after an update | Refresh with **Ctrl+F5**. If `judge.py` or `app.py` changed, close the judge window and start it again. |

---

## For the maintainer: adding problems

```
problems/<slug>/
  problem.json   {"title", "difficulty": Easy|Medium|Hard, "time_limit_ms", "memory_mb",
                  "order" (optional), "float_tolerance" (optional, relative)}
  statement.md   Markdown with $math$ (KaTeX). Samples are shown automatically from tests/sample*.
  tests/         sample1.in/.out ... plus any other *.in/*.out
  _author/       solution.cpp|py (reference), brute.cpp|py, gen.py  (kept out of Git)
```

Build and verify the tests with `python tools/build_tests.py <slug>`. It generates inputs, writes the expected
outputs from the reference solution, stress-tests the brute force against the reference, then judges the
reference (it must get Accepted). Then commit `problems/<slug>` and push.
