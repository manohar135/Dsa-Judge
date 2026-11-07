You are given an integer array `processes` of size `n`, where each element is the time required to complete a process, and the total available time `T`.

A CPU scheduler executes processes alternately from both ends of the array:

1. The first unit of time goes to the leftmost unfinished process.
2. The next unit goes to the rightmost unfinished process.
3. The CPU keeps alternating: left, right, left, right, ... Each unit always goes to the *current* leftmost (or rightmost) unfinished process.
4. Each unit decreases that process's remaining time by 1. When a process's remaining time reaches 0 it is completed, and that side moves inward to the next unfinished process.
5. When only one unfinished process is left, it is both the leftmost and the rightmost, so it receives every unit.
6. This continues until `T` units have been used or all processes are completed.

Return the number of processes completed within `T` units.

### Input
```
n T
processes[0] ... processes[n-1]
```

### Output
A single integer: the number of completed processes.

### Constraints
- 1 ≤ n ≤ 10^5
- 1 ≤ processes[i] ≤ 10^9
- 1 ≤ T ≤ 10^15 (use 64-bit integers)

### Explanation of Example 1
Units: L→p0 (1 left), R→p2 (done), L→p0 (done), R→p1 (2 left), L→p1 (1 left). Two processes are done after 5 units.

### Explanation of Example 2
L→p0, R→p3, L→p0, R→p3, L→p0 (done at unit 5), R→p3. Only p0 is done.

### Explanation of Example 3
Everything finishes in 3 units.
