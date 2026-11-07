# Q7. Earliest Common Free Slot

Run: `python driver.py -7`  ·  Edit: `solution.cpp` in this folder
Category: Intervals / Sorting  ·  Source: WhatsApp list: "intervals where people are busy... find min starting time where people can be free for k hrs" (also IIITH compendium, 4.6)

## Problem Description

You are given the busy intervals of a group of people, all merged into one list: `busy[i] = [start_i, end_i]` means *someone* is busy during the half-open time range `[start_i, end_i)`. Time starts at 0. Intervals may overlap, nest or touch, and are given in any order.

Find the earliest time `t ≥ 0` such that **nobody** is busy at any moment of `[t, t + k)`.

## Function signature

```cpp
// busy : busy[i] = {start, end}, someone is busy during [start, end)
// k : length of the free slot needed
// Return the earliest t >= 0 such that nobody is busy during [t, t + k).
long long earliestFreeStart(vector<vector<int>>& busy, int k);
```

## Input Format

```
n k
start_0 end_0
...
start_{n-1} end_{n-1}
```

## Output Format

A single integer: the earliest valid start time `t`.

## Constraints

- 1 ≤ n ≤ 10^5
- 1 ≤ k ≤ 10^9
- 0 ≤ start_i < end_i ≤ 10^9
- The answer is at most 10^9 (it always exists, since time is unbounded after the last meeting).

## Example 1

Input:
```
3 3
1 3
2 5
8 10
```
Output:
```
5
```
Explanation: Free gaps: [0,1) (too short) and [5,8) (length 3). So t = 5.

## Example 2

Input:
```
2 2
0 2
3 4
```
Output:
```
4
```
Explanation: The gap [2,3) is only 1 long; after time 4 everyone is free.

## Example 3

Input:
```
1 4
4 6
```
Output:
```
0
```
Explanation: [0,4) is free.

## Notes / Assumptions

- Intervals are **half-open**: a meeting `[1, 3)` ends at 3, so a slot may start exactly at 3, and a slot `[t, t+k)` may end exactly when a meeting starts.
- Everyone's intervals are given as one combined list (who is busy doesn't matter, only when).
- There is no end of day: if no gap fits, the answer is the end of the last meeting.
