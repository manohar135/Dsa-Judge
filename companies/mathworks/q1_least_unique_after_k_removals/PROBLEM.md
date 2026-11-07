# Q1. Least Number of Unique Integers after K Removals

Run: `python driver.py -1`  ·  Edit: `solution.cpp` in this folder
Category: Greedy / Hash map / Sorting  ·  Source: WhatsApp list: "Leetcode 1481"

## Problem Description

Given an array of integers `arr` and an integer `k`, find the least number of unique (distinct) integers left in the array after removing **exactly** `k` elements.

## Function signature

```cpp
// arr : the array, k : exactly how many elements you must remove
// Return the least number of distinct integers left after removing exactly k elements.
int findLeastNumOfUniqueInts(vector<int>& arr, int k);
```

## Input Format

```
n k
arr[0] arr[1] ... arr[n-1]
```

## Output Format

A single integer: the least number of distinct values left.

## Constraints

- 1 ≤ n ≤ 10^5
- 1 ≤ arr[i] ≤ 10^9
- 0 ≤ k ≤ n

## Example 1

Input:
```
3 1
5 5 4
```
Output:
```
1
```
Explanation: Remove the single 4; only 5 is left.

## Example 2

Input:
```
7 3
4 3 1 1 3 3 2
```
Output:
```
2
```
Explanation: Remove 4, 2 and one of the 1s. The values 1 and 3 are left.
