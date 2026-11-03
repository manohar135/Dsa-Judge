A degree has $n$ modules numbered $1$ to $n$. Some modules have prerequisites: each pair $[a, b]$ in `prereqs` means module $a$ must be finished in an **earlier** semester than module $b$.

A student can take any number of modules in one semester, as long as all their prerequisites were finished in earlier semesters.

Find the minimum number of semesters needed to finish all $n$ modules. If the prerequisites contain a cycle, so that some modules can never be taken, return `-1`.

### Input
- The first line contains two space-separated integers $n$ and $m$ — the number of modules and the number of prerequisite pairs.
- Each of the next $m$ lines contains two space-separated integers $a$ and $b$, meaning module $a$ must be finished before module $b$.

### Output
Print a single integer — the minimum number of semesters needed to finish all $n$ modules, or `-1` if it is impossible.

### Constraints
- $1 \le n \le 10^5$
- $0 \le m \le 10^5$
- $1 \le a, b \le n$, $a \ne b$
- No pair $[a, b]$ appears twice.

### Explanation of Example 1
- **Semester 1:** module $1$ (no prerequisites)
- **Semester 2:** modules $2$ and $4$ (both need only module $1$)
- **Semester 3:** module $3$ (needs module $2$)

The longest prerequisite chain $1 \to 2 \to 3$ has $3$ modules, so $3$ semesters are required.

### Explanation of Example 2
Module $1$ needs $2$ and module $2$ needs $1$. Neither can ever be started, so the answer is `-1`.

### Explanation of Example 3
With $0$ prerequisites, all $5$ modules can be taken together in Semester 1.

