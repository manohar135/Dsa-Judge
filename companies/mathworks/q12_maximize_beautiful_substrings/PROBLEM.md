# Q12. Maximize Beautiful Substrings

Run: `python driver.py -12`  ·  Edit: `solution.cpp` in this folder
Category: Greedy / Dynamic Programming  ·  Source: MathWorks (IITB) Question 3

## Problem Description

You are given a string consisting of lowercase English letters (`a`–`z`) and dots (`.`).

Replace each dot with any lowercase English letter so that the total number of beautiful substrings is maximized.

A beautiful substring is a contiguous segment consisting entirely of identical characters. Substrings at different positions are counted separately.

## Function signature

```cpp
// s : lowercase letters and '.'
// Return the maximum number of beautiful substrings after replacing every '.' (64-bit).
long long maxBeautifulSubstrings(string s);
```

## Input Format

```
s
```

## Output Format

An integer representing the maximum possible total number of beautiful substrings after replacing all dots.

## Constraints

- 1 ≤ |s| ≤ 10^5
- `s` consists of lowercase letters and `.`
- The answer can reach about 5·10^9: use 64-bit integers.

## Example 1

Input:
```
a.b
```
Output:
```
4
```
Explanation: "aab": a, a, aa, b → 4 ("abb" is also 4).

## Example 2

Input:
```
aa..b
```
Output:
```
11
```
Explanation: "aaaab": the run aaaa gives 4·5/2 = 10, plus b → 11.

## Example 3

Input:
```
...
```
Output:
```
6
```
Explanation: "aaa": 3 + 2 + 1 = 6.

## Notes / Assumptions

- A run of `L` equal letters contains `L·(L+1)/2` beautiful substrings.
- No constraints were given; |s| ≤ 10^5 was assumed.
