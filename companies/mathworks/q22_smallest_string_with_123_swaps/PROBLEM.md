# Q22. Smallest String with 1-2-3 Swaps

Run: `python driver.py -22`  ·  Edit: `solution.cpp` in this folder
Category: Greedy / Strings  ·  Source: MathWorks IIITH 2026, Engineering group coding question 3.1 (Number Game)

## Problem Description

You are given a string `S` of digits `1`, `2` and `3`. You may repeatedly apply two kinds of adjacent swaps:

- `"21"` becomes `"12"`
- `"32"` becomes `"23"`

No other swap is allowed (in particular, adjacent `1` and `3` may never be swapped, and the swaps never go the other way).

Return the lexicographically smallest string that can be reached.

## Function signature

```cpp
// s : a string of digits '1', '2', '3'
// Return the lexicographically smallest string reachable with the allowed swaps.
string numberGame(string s);
```

## Input Format

```
S
```

## Output Format

The smallest reachable string.

## Constraints

- 1 ≤ |S| ≤ 10^5
- `S` consists only of `1`, `2`, `3`.

## Example 1

Input:
```
321
```
Output:
```
231
```
Explanation: "32" → "23" gives 231. No more swaps apply.

## Example 2

Input:
```
2213
```
Output:
```
1223
```
Explanation: 2213 → 2123 → 1223.

## Example 3

Input:
```
3122
```
Output:
```
3122
```
Explanation: No "21" or "32" pair exists, so nothing can move.

## Notes / Assumptions

- Example 3 was added (computed by brute force over all reachable strings).
