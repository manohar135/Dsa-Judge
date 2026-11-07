# Q11. Scatter Palindrome Substrings

Run: `python driver.py -11`  ·  Edit: `solution.cpp` in this folder
Category: Bitmask / Prefix XOR / Hashing  ·  Source: MathWorks (IITB) Question 2, and the MathWorks CS OA PDF, problem 2

## Problem Description

You are given a vector of strings. For each string, count the number of contiguous substrings whose characters can be rearranged to form a palindrome (a *scatter palindrome*).

Substrings at different positions are counted separately, even if they are equal. Return the count for each string.

## Function signature

```cpp
// strs : the strings
// Return, for each string, the number of its substrings that can be rearranged into a palindrome.
vector<long long> countScatterPalindromes(vector<string>& strs);
```

## Input Format

```
N
s_1
...
s_N
```

## Output Format

`N` lines: the count for each string, in input order.

## Constraints

- 1 ≤ N ≤ 100
- 1 ≤ |s_i| ≤ 1000
- Strings consist of lowercase English letters.

## Example 1

Input:
```
1
aabb
```
Output:
```
9
```
Explanation: Single letters (4), aa and bb (2), aab and abb (2), and aabb (1). "ab" can't be rearranged into a palindrome.

## Example 2

Input:
```
2
abc
aaa
```
Output:
```
3
6
```
Explanation: "abc": only the 3 single letters. "aaa": all 6 substrings.

## Example 3

Input:
```
1
bbrrg
```
Output:
```
12
```
Explanation: 5 single letters, bb, rr, bbr, brr, rrg, bbrr, bbrrg → 12.

## Notes / Assumptions

- The PDF's example text was self-contradictory ("abca qualifies... actually it does not"). The rule used is the standard one: a substring qualifies when **at most one** letter has an odd count.
