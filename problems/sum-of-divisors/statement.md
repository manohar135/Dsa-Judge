You are given an array `nums`. For every element `nums[i]`, find the sum of all of its positive divisors (factors), including 1 and `nums[i]` itself.

Return the results in the same order as the input.

### Input
```
n
nums[0] nums[1] ... nums[n-1]
```

### Output
`n` lines; line `i` holds the divisor sum of `nums[i]`.

### Constraints
- 1 ≤ n ≤ 10^5
- 1 ≤ nums[i] ≤ 10^6
- Every divisor sum here is below 5·10^6 (it fits in `int`; the method returns `long long` anyway).

### Explanation of Example 1
6 → 1+2+3+6 = 12; 1 → 1; 12 → 1+2+3+4+6+12 = 28.

### Explanation of Example 2
7 → 1+7; 9 → 1+3+9; 10 → 1+2+5+10.
