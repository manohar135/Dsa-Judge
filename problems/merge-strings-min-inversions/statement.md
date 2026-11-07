You are given two strings `a` and `b`. Merge them into one string `t` of length `|a| + |b|` such that the characters of `a` appear in `t` in their original order and the characters of `b` appear in `t` in their original order (any interleaving is allowed).

An **inversion** of `t` is a pair of indices `i < j` with `t[i] > t[j]` (comparing letters alphabetically).

Return the minimum possible number of inversions of `t`.

### Input
```
a
b
```

### Output
A single integer: the minimum number of inversions.

### Constraints
- 1 ≤ |a|, |b| ≤ 1000
- Both strings consist of lowercase English letters.

### Explanation of Example 1
Possible merges: bca (2 inversions: b>a, c>a), cba (3), cab (2). The minimum is 2.

### Explanation of Example 2
Take b's 'a', then a's 'b', then a's 'a', then b's 'b': "abab" has 1 inversion (the b at index 1 before the a at index 2). Zero is impossible, because a's 'b' must come before a's 'a'.
