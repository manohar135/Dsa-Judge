Given an array `a` of positive integers, count the subarrays (contiguous, non-empty) whose product is a perfect square.

### Input
```
n
a[0] ... a[n-1]
```

### Output
A single integer: the number of such subarrays.

### Constraints
- 1 ≤ n ≤ 2·10^5
- 1 ≤ a[i] ≤ 200
- The answer can reach about 2·10^10: use 64-bit integers.

### Explanation of Example 1
[2, 8] = 16, [3, 12] = 36 and [2, 8, 3, 12] = 576 = 24².

### Explanation of Example 2
Every product is 1.

### Explanation of Example 3
Only the whole array: 5·7·35 = 1225 = 35².
