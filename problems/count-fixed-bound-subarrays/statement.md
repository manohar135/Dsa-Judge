You are given an integer array `prices` of size `n`, representing the stock prices on `n` consecutive days. You are also given two integers, `minK` and `maxK`, representing the required minimum and maximum stock prices.

Count the total number of contiguous subarrays such that:

1. The minimum element in the subarray is exactly `minK`.
2. The maximum element in the subarray is exactly `maxK`.

A subarray containing any element smaller than `minK` or greater than `maxK` is invalid.

### Input
```
n minK maxK
prices[0] ... prices[n-1]
```

### Output
A single integer: the number of valid subarrays.

### Constraints
- 1 ≤ n ≤ 10^5
- 1 ≤ prices[i], minK, maxK ≤ 10^6
- The answer can reach about 5·10^9: use 64-bit integers.

### Explanation of Example 1
[1, 3, 5] and [1, 3, 5, 2].

### Explanation of Example 2
Every one of the 10 subarrays has min = max = 1.
