You are given an integer array. Partition the array into the minimum possible number of subsequences such that every subsequence has a majority element.

A majority element is an element that occurs strictly more than half the length of that subsequence.

Every element must belong to exactly one subsequence. Find the minimum number of subsequences required.

### Input
```
n
nums[0] nums[1] ... nums[n-1]
```

### Output
A single integer: the minimum number of subsequences.

### Constraints
- 1 ≤ n ≤ 10^5
- 1 ≤ nums[i] ≤ 10^9

### Explanation of Example 1
1 appears 3 > 5/2 times, so the whole array is one valid subsequence.

### Explanation of Example 2
All values are distinct, so any subsequence with 2 or more elements has no majority. Every element stands alone.

### Explanation of Example 3
{1, 1, 2} (1 is the majority) and {2, 3, 3} (3 is the majority).
