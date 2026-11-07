# Q6. Merge Two Strings with Minimum Inversions

Run: `python driver.py -6`  ·  Edit: `solution.cpp` in this folder
Category: Dynamic Programming  ·  Source: WhatsApp list: "merge 2 strings such that both relative order preserved but min inversion count" (also IIITH compendium, 4.5)

## Problem Description

You are given two strings `a` and `b`. Merge them into one string `t` of length `|a| + |b|` such that the characters of `a` appear in `t` in their original order and the characters of `b` appear in `t` in their original order (any interleaving is allowed).

An **inversion** of `t` is a pair of indices `i < j` with `t[i] > t[j]` (comparing letters alphabetically).

Return the minimum possible number of inversions of `t`.

## Function signature

```cpp
// a, b : the two strings to merge (each keeps its own order)
// Return the minimum number of inversions of the merged string.
long long minMergeInversions(string a, string b);
```

## Input Format

```
a
b
```

## Output Format

A single integer: the minimum number of inversions.

## Constraints

- 1 ≤ |a|, |b| ≤ 1000
- Both strings consist of lowercase English letters.

## Example 1

Input:
```
ca
b
```
Output:
```
2
```
Explanation: Possible merges: bca (2 inversions: b>a, c>a), cba (3), cab (2). The minimum is 2.

## Example 2

Input:
```
ba
ab
```
Output:
```
1
```
Explanation: Take b's 'a', then a's 'b', then a's 'a', then b's 'b': "abab" has 1 inversion (the b at index 1 before the a at index 2). Zero is impossible, because a's 'b' must come before a's 'a'.

## Notes / Assumptions

- Inversions inside `a` and inside `b` count too (they're part of `t`). The order of each string is fixed, so those can't be avoided.
- Letters are compared alphabetically; equal letters are not an inversion.
- No constraints were recalled; |a|, |b| ≤ 1000 makes an O(|a|·|b|) DP the target.
