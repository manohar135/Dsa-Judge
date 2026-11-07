# Q2. Minimum Number of Groups to Create a Valid Assignment

Run: `python driver.py -2`  ·  Edit: `solution.cpp` in this folder
Category: Greedy / Math / Counting  ·  Source: WhatsApp list: "Leetcode 2910"

## Problem Description

You are given an array `nums` of `n` balls; `nums[i]` is the number written on ball `i`. Put every ball into exactly one group so that:

1. All balls in the same group have the same number.
2. The sizes of any two groups differ by at most 1.

Return the minimum number of groups.

## Function signature

```cpp
// nums : the balls (values)
// Return the minimum number of groups in a valid assignment.
int minGroupsForValidAssignment(vector<int>& nums);
```

## Input Format

```
n
nums[0] nums[1] ... nums[n-1]
```

## Output Format

A single integer: the minimum number of groups.

## Constraints

- 1 ≤ n ≤ 10^5
- 1 ≤ nums[i] ≤ 10^9

## Example 1

Input:
```
5
3 2 3 2 3
```
Output:
```
2
```
Explanation: Groups {3,3,3} and {2,2}: sizes 3 and 2 differ by 1.

## Example 2

Input:
```
6
10 10 10 3 1 1
```
Output:
```
4
```
Explanation: Groups {10}, {10,10}, {3}, {1,1}: sizes are 1 or 2.
