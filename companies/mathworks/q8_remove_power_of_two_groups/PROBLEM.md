# Q8. Remove Power-of-Two Groups

Run: `python driver.py -8`  ·  Edit: `solution.cpp` in this folder
Category: Greedy / Bit manipulation  ·  Source: WhatsApp list: "we can select any numbers... 2^2 + 2^4 + 2^5 should be 2^p then we can remove them, min steps to empty the array" (also IIITH compendium, 4.7)

## Problem Description

You are given an array `w` of `n` exponents; element `i` has weight `2^w[i]`.

In one step you may choose any non-empty set of the remaining elements whose total weight is a power of two, i.e. `2^{w[i1]} + 2^{w[i2]} + ... + 2^{w[im]} = 2^p` for some integer `p ≥ 0`, and remove them all.

Return the minimum number of steps needed to remove every element.

## Function signature

```cpp
// w : the exponents; element i has weight 2^w[i]
// Return the minimum number of steps to remove every element.
int minSteps(vector<int>& w);
```

## Input Format

```
n
w[0] w[1] ... w[n-1]
```

## Output Format

A single integer: the minimum number of steps.

## Constraints

- 1 ≤ n ≤ 3·10^5
- 0 ≤ w[i] ≤ 10^6 (weights are far too large to store directly)

## Example 1

Input:
```
5
1 1 2 3 3
```
Output:
```
2
```
Explanation: Remove {1, 1, 2, 3} (2 + 2 + 4 + 8 = 16 = 2^4), then {3} (8 = 2^3).

## Example 2

Input:
```
4
0 1 2 3
```
Output:
```
4
```
Explanation: 1, 2, 4 and 8 can't be grouped into a power of two in any way, so each needs its own step.

## Example 3

Input:
```
5
2 4 3 5 6
```
Output:
```
5
```
Explanation: All exponents differ, so every element must go alone.

## Notes / Assumptions

- The array holds the **exponents** (the recalled example "[2,4,3,5,6] ... 2^2+2^4+2^5" uses them that way). This is the same task as Codeforces 587A.
- No constraints were recalled beyond "array length 10^5"; I used n ≤ 3·10^5 and exponents up to 10^6.
