# Q23. Perfect-Square Product Subarrays

Run: `python driver.py -23`  ·  Edit: `solution.cpp` in this folder
Category: Bitmask / Prefix XOR / Hashing  ·  Source: MathWorks IIITH 2026, additional problem 4.2

## Problem Description

Given an array `a` of positive integers, count the subarrays (contiguous, non-empty) whose product is a perfect square.

## Function signature

```cpp
// nums : the array (1 <= nums[i] <= 200)
// Return the number of subarrays whose product is a perfect square (64-bit).
long long countSquareProductSubarrays(vector<int>& nums);
```

## Input Format

```
n
a[0] ... a[n-1]
```

## Output Format

A single integer: the number of such subarrays.

## Constraints

- 1 ≤ n ≤ 2·10^5
- 1 ≤ a[i] ≤ 200
- The answer can reach about 2·10^10: use 64-bit integers.

## Example 1

Input:
```
4
2 8 3 12
```
Output:
```
3
```
Explanation: [2, 8] = 16, [3, 12] = 36 and [2, 8, 3, 12] = 576 = 24².

## Example 2

Input:
```
3
1 1 1
```
Output:
```
6
```
Explanation: Every product is 1.

## Example 3

Input:
```
3
5 7 35
```
Output:
```
1
```
Explanation: Only the whole array: 5·7·35 = 1225 = 35².

## Notes / Assumptions

- The compendium gave n up to 10^5; I raised it to 2·10^5 so an O(n²) scan reliably times out. Examples were written for this kit (no examples were recalled).
