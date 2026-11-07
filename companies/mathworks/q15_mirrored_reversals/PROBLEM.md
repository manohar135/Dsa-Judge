# Q15. Mirrored Reversals

Run: `python driver.py -15`  ·  Edit: `solution.cpp` in this folder
Category: Strings / Prefix parity  ·  Source: MathWorks Q3 ("for each number[i] reverse the string from numbers[i] to s.size()-1-numbers[i]")

## Problem Description

You are given a string `s` of length `n` and a list of integers `positions`. Process them in order: for each `x`, reverse the substring `s[x .. n-1-x]` (0-indexed, both ends inclusive).

Return the final string.

## Function signature

```cpp
// s : the string, positions : for each x, reverse s[x .. n-1-x] (0-indexed, inclusive)
// Return the string after all reversals.
string applyReversals(string s, vector<int>& positions);
```

## Input Format

```
s
m
positions[0] ... positions[m-1]
```

## Output Format

The final string.

## Constraints

- 1 ≤ n ≤ 2·10^5, `s` consists of lowercase letters
- 1 ≤ m ≤ 10^5
- 0 ≤ positions[i] and 2·positions[i] ≤ n − 1 (so the segment is never empty)

## Example 1

Input:
```
abcdef
1
1
```
Output:
```
aedcbf
```
Explanation: Reverse s[1..4] = "bcde".

## Example 2

Input:
```
vwxyz
2
1 1
```
Output:
```
vwxyz
```
Explanation: Reversing the same segment twice changes nothing.

## Example 3

Input:
```
abcdef
3
2 1 0
```
Output:
```
fbdcea
```
Explanation: abcdef → abdcef → aecdbf → fbdcea.

## Notes / Assumptions

- Positions are 0-indexed, as in the recollection (`numbers[i]` to `s.size()-1-numbers[i]`). This is Codeforces 525B with 0-based indices.
- No constraints were recalled; with these sizes, reversing each segment directly times out.
