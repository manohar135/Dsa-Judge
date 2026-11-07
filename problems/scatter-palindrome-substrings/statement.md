You are given a vector of strings. For each string, count the number of contiguous substrings whose characters can be rearranged to form a palindrome (a *scatter palindrome*).

Substrings at different positions are counted separately, even if they are equal. Return the count for each string.

### Input
```
N
s_1
...
s_N
```

### Output
`N` lines: the count for each string, in input order.

### Constraints
- 1 ≤ N ≤ 100
- 1 ≤ |s_i| ≤ 1000
- Strings consist of lowercase English letters.

### Explanation of Example 1
Single letters (4), aa and bb (2), aab and abb (2), and aabb (1). "ab" can't be rearranged into a palindrome.

### Explanation of Example 2
"abc": only the 3 single letters. "aaa": all 6 substrings.

### Explanation of Example 3
5 single letters, bb, rr, bbr, brr, rrg, bbrr, bbrrg → 12.
