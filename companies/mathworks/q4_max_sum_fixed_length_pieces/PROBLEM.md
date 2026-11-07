# Q4. Maximum Sum of Fixed-Length Pieces

Run: `python driver.py -4`  ·  Edit: `solution.cpp` in this folder
Category: Dynamic Programming  ·  Source: WhatsApp list: "2. We can take subarray of length 1 x times, 2 y times and length 3 z times ... largest sum ... should not overlap"

## Problem Description

You are given an integer array `nums` and three integers `x`, `y`, `z`.

You must choose **exactly** `x` subarrays of length 1, **exactly** `y` subarrays of length 2 and **exactly** `z` subarrays of length 3. No two chosen subarrays may overlap (they may touch). Elements that are not inside any chosen subarray are ignored.

Return the largest possible total sum of all elements inside the chosen subarrays.

## Function signature

```cpp
// nums : the array, x / y / z : how many pieces of length 1 / 2 / 3 you must take
// Return the maximum total sum of x+y+z non-overlapping pieces (64-bit).
long long maxSumOfPieces(vector<int>& nums, int x, int y, int z);
```

## Input Format

```
n x y z
nums[0] nums[1] ... nums[n-1]
```

## Output Format

A single integer: the maximum total (can be negative).

## Constraints

- 1 ≤ n ≤ 300
- 0 ≤ x, y, z ≤ 25 and x + 2y + 3z ≤ n (a valid choice always exists)
- −10^9 ≤ nums[i] ≤ 10^9
- The answer can reach about 1.5·10^11 in absolute value: use 64-bit integers.

## Example 1

Input:
```
6 1 1 0
1 -2 3 4 -1 2
```
Output:
```
9
```
Explanation: Take [3, 4] as the length-2 piece and [2] as the length-1 piece: 7 + 2 = 9.

## Example 2

Input:
```
6 1 1 1
5 -10 5 5 -1 6
```
Output:
```
10
```
Explanation: x + 2y + 3z = 6 = n, so the pieces cover the whole array, e.g. [5], [-10, 5], [5, -1, 6]. The total is the sum of the array, 10.

## Notes / Assumptions

- The recalled statement didn't say whether the counts are exact or "at most". I assumed **exactly** x, y and z pieces (so negative numbers may be forced into the answer).
- No constraints were recalled. I chose small ones (n ≤ 300, counts ≤ 25) so the intended DP over (position, pieces used) fits; plain recursion without memoisation times out.
