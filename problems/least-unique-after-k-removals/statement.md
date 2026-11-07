Given an array of integers `arr` and an integer `k`, find the least number of unique (distinct) integers left in the array after removing **exactly** `k` elements.

### Input
```
n k
arr[0] arr[1] ... arr[n-1]
```

### Output
A single integer: the least number of distinct values left.

### Constraints
- 1 ≤ n ≤ 10^5
- 1 ≤ arr[i] ≤ 10^9
- 0 ≤ k ≤ n

### Explanation of Example 1
Remove the single 4; only 5 is left.

### Explanation of Example 2
Remove 4, 2 and one of the 1s. The values 1 and 3 are left.
