# Q10. Minimum Subsequences with a Majority Element

Run: `python driver.py -10`  ·  Edit: `solution.cpp` in this folder
Category: Greedy / Counting  ·  Source: MathWorks (IITB) Question 1

## Problem Description

You are given an integer array. Partition the array into the minimum possible number of subsequences such that every subsequence has a majority element.

A majority element is an element that occurs strictly more than half the length of that subsequence.

Every element must belong to exactly one subsequence. Find the minimum number of subsequences required.

## Function signature

```cpp
// nums : the array
// Return the minimum number of subsequences, each having a strict majority element.
int minSubsequences(vector<int>& nums);
```

## Input Format

```
n
nums[0] nums[1] ... nums[n-1]
```

## Output Format

A single integer: the minimum number of subsequences.

## Constraints

- 1 ≤ n ≤ 10^5
- 1 ≤ nums[i] ≤ 10^9

## Example 1

Input:
```
5
1 2 1 3 1
```
Output:
```
1
```
Explanation: 1 appears 3 > 5/2 times, so the whole array is one valid subsequence.

## Example 2

Input:
```
4
1 2 3 4
```
Output:
```
4
```
Explanation: All values are distinct, so any subsequence with 2 or more elements has no majority. Every element stands alone.

## Example 3

Input:
```
6
1 1 2 2 3 3
```
Output:
```
2
```
Explanation: {1, 1, 2} (1 is the majority) and {2, 3, 3} (3 is the majority).

## Notes / Assumptions

- A subsequence of length 1 always has a majority element.
- No constraints were given; n ≤ 10^5 was assumed.
