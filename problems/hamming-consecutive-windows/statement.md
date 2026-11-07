You are given a string `s` of length `n` and an integer `k`. Consider every substring of length `k` (window) in order: `W_0 = s[0..k-1]`, `W_1 = s[1..k]`, ..., `W_{n-k} = s[n-k..n-1]`.

For every pair of consecutive windows `W_i` and `W_{i+1}` (0 ≤ i < n − k), compute their Hamming distance: the number of positions `j` (0 ≤ j < k) where `W_i[j] ≠ W_{i+1}[j]`.

Return the `n − k` distances in order.

### Input
```
s
k
```

### Output
`n − k` lines; line `i` holds the Hamming distance between `W_i` and `W_{i+1}`.

### Constraints
- 2 ≤ n = |s| ≤ 2·10^5
- 1 ≤ k < n
- `s` consists of lowercase English letters.

### Explanation of Example 1
Windows: ab, ba, ab. d(ab, ba) = 2 and d(ba, ab) = 2.

### Explanation of Example 2
Windows: aab, abb, bba. d(aab, abb) = 1 (middle letter); d(abb, bba) = 2.
