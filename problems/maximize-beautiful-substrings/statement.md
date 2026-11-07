You are given a string consisting of lowercase English letters (`a`–`z`) and dots (`.`).

Replace each dot with any lowercase English letter so that the total number of beautiful substrings is maximized.

A beautiful substring is a contiguous segment consisting entirely of identical characters. Substrings at different positions are counted separately.

### Input
```
s
```

### Output
An integer representing the maximum possible total number of beautiful substrings after replacing all dots.

### Constraints
- 1 ≤ |s| ≤ 10^5
- `s` consists of lowercase letters and `.`
- The answer can reach about 5·10^9: use 64-bit integers.

### Explanation of Example 1
"aab": a, a, aa, b → 4 ("abb" is also 4).

### Explanation of Example 2
"aaaab": the run aaaa gives 4·5/2 = 10, plus b → 11.

### Explanation of Example 3
"aaa": 3 + 2 + 1 = 6.
