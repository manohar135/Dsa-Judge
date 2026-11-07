You are given an integer array `nums` and three integers `x`, `y`, `z`.

You must choose **exactly** `x` subarrays of length 1, **exactly** `y` subarrays of length 2 and **exactly** `z` subarrays of length 3. No two chosen subarrays may overlap (they may touch). Elements that are not inside any chosen subarray are ignored.

Return the largest possible total sum of all elements inside the chosen subarrays.

### Input
```
n x y z
nums[0] nums[1] ... nums[n-1]
```

### Output
A single integer: the maximum total (can be negative).

### Constraints
- 1 ≤ n ≤ 300
- 0 ≤ x, y, z ≤ 25 and x + 2y + 3z ≤ n (a valid choice always exists)
- −10^9 ≤ nums[i] ≤ 10^9
- The answer can reach about 1.5·10^11 in absolute value: use 64-bit integers.

### Explanation of Example 1
Take [3, 4] as the length-2 piece and [2] as the length-1 piece: 7 + 2 = 9.

### Explanation of Example 2
x + 2y + 3z = 6 = n, so the pieces cover the whole array, e.g. [5], [-10, 5], [5, -1, 6]. The total is the sum of the array, 10.
