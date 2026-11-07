# Q5. Hamming Distance of Consecutive Windows

Run: `python driver.py -5`  ·  Edit: `solution.cpp` in this folder
Category: Strings / Sliding window / Prefix sums  ·  Source: WhatsApp list: "Hamming distance of consecutive substrings of length k over a string s" (also in the IIITH compendium, 4.4)

## Problem Description

You are given a string `s` of length `n` and an integer `k`. Consider every substring of length `k` (window) in order: `W_0 = s[0..k-1]`, `W_1 = s[1..k]`, ..., `W_{n-k} = s[n-k..n-1]`.

For every pair of consecutive windows `W_i` and `W_{i+1}` (0 ≤ i < n − k), compute their Hamming distance: the number of positions `j` (0 ≤ j < k) where `W_i[j] ≠ W_{i+1}[j]`.

Return the `n − k` distances in order.

## Function signature

```cpp
// s : the string, k : window length
// Return d[0..n-k-1], where d[i] = Hamming distance of s[i..i+k-1] and s[i+1..i+k].
vector<int> consecutiveWindowDistances(string s, int k);
```

## Input Format

```
s
k
```

## Output Format

`n − k` lines; line `i` holds the Hamming distance between `W_i` and `W_{i+1}`.

## Constraints

- 2 ≤ n = |s| ≤ 2·10^5
- 1 ≤ k < n
- `s` consists of lowercase English letters.

## Example 1

Input:
```
abab
2
```
Output:
```
2
2
```
Explanation: Windows: ab, ba, ab. d(ab, ba) = 2 and d(ba, ab) = 2.

## Example 2

Input:
```
aabba
3
```
Output:
```
1
2
```
Explanation: Windows: aab, abb, bba. d(aab, abb) = 1 (middle letter); d(abb, bba) = 2.

## Notes / Assumptions

- "Consecutive substrings" was read as **overlapping windows that start one position apart** (the reading used in the IIITH compendium). If you remember non-overlapping blocks `s[0..k-1]`, `s[k..2k-1]`, ..., tell me.
- No constraints were recalled; with n = 2·10^5 the direct O(n·k) comparison times out.
