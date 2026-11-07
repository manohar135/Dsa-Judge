You are given an array `nums` of `n` balls; `nums[i]` is the number written on ball `i`. Put every ball into exactly one group so that:

1. All balls in the same group have the same number.
2. The sizes of any two groups differ by at most 1.

Return the minimum number of groups.

### Input
```
n
nums[0] nums[1] ... nums[n-1]
```

### Output
A single integer: the minimum number of groups.

### Constraints
- 1 ≤ n ≤ 10^5
- 1 ≤ nums[i] ≤ 10^9

### Explanation of Example 1
Groups {3,3,3} and {2,2}: sizes 3 and 2 differ by 1.

### Explanation of Example 2
Groups {10}, {10,10}, {3}, {1,1}: sizes are 1 or 2.
