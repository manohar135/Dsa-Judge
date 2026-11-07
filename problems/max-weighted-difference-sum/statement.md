Given two arrays each of length `n`, `arr1` and `arr2`. In one operation, any two elements of an array can be swapped. This can occur any number of times (each array may be rearranged freely, independently).

Find the maximum possible sum of `i * (arr2[i] - arr1[i])` for all `1 ≤ i ≤ n` after rearranging the arrays.

Since the maximum possible sum can be large, return the value modulo `(10^9 + 7)`.

### Input
```
n
arr1[1] ... arr1[n]
arr2[1] ... arr2[n]
```

### Output
A single integer in [0, 10^9 + 6].

### Constraints
- 1 ≤ n ≤ 10^5
- 1 ≤ arr1[i], arr2[i] ≤ 10^9
- Products `i * arr[i]` exceed 2^31 − 1, and the raw sum can approach 5·10^18.

### Explanation of Example 1
Some rearrangements: ([2,1,3,4], [2,3,2,3]) gives [0,4,-3,-4], sum -3; ([3,1,2,4], [2,3,2,3]) gives -1; ([3,1,2,4], [3,2,2,3]) gives -2. The maximum possible sum is 7, and 7 mod (10^9+7) = 7.

### Explanation of Example 2
The only sum is 1·(2 − 5) = −3, and −3 mod (10^9 + 7) = 1000000004.
