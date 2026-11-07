# Q16. Count Subarrays With Fixed Minimum and Maximum

Run: `python driver.py -16`  ·  Edit: `solution.cpp` in this folder
Category: Sliding window / Two pointers  ·  Source: MathWorks OA (recalled problem 1)

## Problem Description

You are given an integer array `prices` of size `n`, representing the stock prices on `n` consecutive days. You are also given two integers, `minK` and `maxK`, representing the required minimum and maximum stock prices.

Count the total number of contiguous subarrays such that:

1. The minimum element in the subarray is exactly `minK`.
2. The maximum element in the subarray is exactly `maxK`.

A subarray containing any element smaller than `minK` or greater than `maxK` is invalid.

## Function signature

```cpp
// prices : the array, minK / maxK : required minimum / maximum
// Return the number of subarrays whose min is minK and max is maxK (64-bit).
long long countSubarrays(vector<int>& prices, int minK, int maxK);
```

## Input Format

```
n minK maxK
prices[0] ... prices[n-1]
```

## Output Format

A single integer: the number of valid subarrays.

## Constraints

- 1 ≤ n ≤ 10^5
- 1 ≤ prices[i], minK, maxK ≤ 10^6
- The answer can reach about 5·10^9: use 64-bit integers.

## Example 1

Input:
```
6 1 5
1 3 5 2 7 5
```
Output:
```
2
```
Explanation: [1, 3, 5] and [1, 3, 5, 2].

## Example 2

Input:
```
4 1 1
1 1 1 1
```
Output:
```
10
```
Explanation: Every one of the 10 subarrays has min = max = 1.

## Notes / Assumptions

- minK may be greater than maxK; then the answer is 0. Same task as LeetCode 2444.
