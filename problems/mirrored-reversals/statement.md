You are given a string `s` of length `n` and a list of integers `positions`. Process them in order: for each `x`, reverse the substring `s[x .. n-1-x]` (0-indexed, both ends inclusive).

Return the final string.

### Input
```
s
m
positions[0] ... positions[m-1]
```

### Output
The final string.

### Constraints
- 1 ≤ n ≤ 2·10^5, `s` consists of lowercase letters
- 1 ≤ m ≤ 10^5
- 0 ≤ positions[i] and 2·positions[i] ≤ n − 1 (so the segment is never empty)

### Explanation of Example 1
Reverse s[1..4] = "bcde".

### Explanation of Example 2
Reversing the same segment twice changes nothing.

### Explanation of Example 3
abcdef → abdcef → aecdbf → fbdcea.
