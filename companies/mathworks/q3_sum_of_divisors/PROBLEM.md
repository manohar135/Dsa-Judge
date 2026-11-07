# Q3. Sum of Divisors of Every Element

Run: `python driver.py -3`  ·  Edit: `solution.cpp` in this folder
Category: Math / Sieve  ·  Source: WhatsApp list: "1. Find sum of factors for all elements in given array"

## Problem Description

You are given an array `nums`. For every element `nums[i]`, find the sum of all of its positive divisors (factors), including 1 and `nums[i]` itself.

Return the results in the same order as the input.

## Function signature

```cpp
// nums : the array
// Return, for every nums[i], the sum of all positive divisors of nums[i].
vector<long long> sumOfDivisors(vector<int>& nums);
```

## Input Format

```
n
nums[0] nums[1] ... nums[n-1]
```

## Output Format

`n` lines; line `i` holds the divisor sum of `nums[i]`.

## Constraints

- 1 ≤ n ≤ 10^5
- 1 ≤ nums[i] ≤ 10^6
- Every divisor sum here is below 5·10^6 (it fits in `int`; the method returns `long long` anyway).

## Example 1

Input:
```
3
6 1 12
```
Output:
```
12
1
28
```
Explanation: 6 → 1+2+3+6 = 12; 1 → 1; 12 → 1+2+3+4+6+12 = 28.

## Example 2

Input:
```
3
7 9 10
```
Output:
```
8
13
18
```
Explanation: 7 → 1+7; 9 → 1+3+9; 10 → 1+2+5+10.

## Notes / Assumptions

- The recalled line was only "find sum of factors for all elements". I read *factors* as **all positive divisors** and return **one sum per element** (not one grand total). If your OA meant something else (prime factors, or a single total), tell me and I'll regenerate.
- No constraints were recalled; `n ≤ 10^5`, `nums[i] ≤ 10^6` were chosen so that an O(value) loop per element is too slow.
