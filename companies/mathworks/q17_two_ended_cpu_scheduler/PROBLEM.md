# Q17. Two-Ended CPU Scheduler

Run: `python driver.py -17`  ·  Edit: `solution.cpp` in this folder
Category: Simulation / Two pointers  ·  Source: MathWorks OA (recalled problem 2)

## Problem Description

You are given an integer array `processes` of size `n`, where each element is the time required to complete a process, and the total available time `T`.

A CPU scheduler executes processes alternately from both ends of the array:

1. The first unit of time goes to the leftmost unfinished process.
2. The next unit goes to the rightmost unfinished process.
3. The CPU keeps alternating: left, right, left, right, ... Each unit always goes to the *current* leftmost (or rightmost) unfinished process.
4. Each unit decreases that process's remaining time by 1. When a process's remaining time reaches 0 it is completed, and that side moves inward to the next unfinished process.
5. When only one unfinished process is left, it is both the leftmost and the rightmost, so it receives every unit.
6. This continues until `T` units have been used or all processes are completed.

Return the number of processes completed within `T` units.

## Function signature

```cpp
// processes : time each process needs, T : total time units available (64-bit)
// Return how many processes are fully completed within T units.
int maxCompletedProcesses(vector<int>& processes, long long T);
```

## Input Format

```
n T
processes[0] ... processes[n-1]
```

## Output Format

A single integer: the number of completed processes.

## Constraints

- 1 ≤ n ≤ 10^5
- 1 ≤ processes[i] ≤ 10^9
- 1 ≤ T ≤ 10^15 (use 64-bit integers)

## Example 1

Input:
```
3 5
2 3 1
```
Output:
```
2
```
Explanation: Units: L→p0 (1 left), R→p2 (done), L→p0 (done), R→p1 (2 left), L→p1 (1 left). Two processes are done after 5 units.

## Example 2

Input:
```
4 6
3 1 2 4
```
Output:
```
1
```
Explanation: L→p0, R→p3, L→p0, R→p3, L→p0 (done at unit 5), R→p3. Only p0 is done.

## Example 3

Input:
```
3 100
1 1 1
```
Output:
```
3
```
Explanation: Everything finishes in 3 units.

## Notes / Assumptions

- The alternation never resets: after a left unit, the next unit always goes right, even if the left process just finished.
- A process that finishes exactly at unit `T` counts.
- No constraints were recalled; with T up to 10^15 a unit-by-unit simulation is too slow.
