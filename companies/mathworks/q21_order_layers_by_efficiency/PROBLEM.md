# Q21. Order Layers by Efficiency

Run: `python driver.py -21`  ·  Edit: `solution.cpp` in this folder
Category: Greedy  ·  Source: MathWorks CS OA PDF, problem 3 ("Minimum Operations to Make Efficiencies Strictly Increasing")

## Problem Description

A neural network has `n` layers. Layer `i` (0-indexed) starts at depth `i + 1`, has an efficiency `efficiency[i]` (all efficiencies are distinct, a permutation of 1..n) and an increment `incr[i]`.

In one operation you pick a layer `i` and increase its depth by `incr[i]`. Depths can only increase.

Find the minimum number of operations so that when the layers are ordered by depth, their efficiencies are **strictly increasing**. In other words, for every two layers, the one with the lower efficiency must end up at a strictly smaller depth.

## Function signature

```cpp
// efficiency : a permutation of 1..n, incr : depth increase per operation
// Layer i (0-indexed) starts at depth i+1. Return the minimum number of operations (64-bit).
long long minOperations(vector<int>& efficiency, vector<int>& incr);
```

## Input Format

```
n
efficiency[0] ... efficiency[n-1]
incr[0] ... incr[n-1]
```

## Output Format

A single integer: the minimum number of operations.

## Constraints

- 1 ≤ n ≤ 10^5
- `efficiency` is a permutation of 1..n
- 1 ≤ incr[i] ≤ 10^4
- The answer can reach about 5·10^9: use 64-bit integers.

## Example 1

Input:
```
3
3 1 2
1 1 1
```
Output:
```
3
```
Explanation: Layers at depths 1, 2, 3 have efficiencies 3, 1, 2. The efficiency-3 layer must go below depth 3: three operations take it to depth 4.

## Example 2

Input:
```
2
2 1
1 3
```
Output:
```
2
```
Explanation: The efficiency-1 layer is at depth 2, so the efficiency-2 layer (depth 1, incr 1) must reach depth 3: two operations.

## Example 3

Input:
```
3
1 2 3
5 5 5
```
Output:
```
0
```
Explanation: Already in order.

## Notes / Assumptions

- The PDF itself says the wording was reconstructed and the exact rule wasn't preserved. I used the standard form of this task (it matches the Codeforces *frog sort* setup: positions, weights and jump lengths): depth = position, efficiency = weight, incr = jump length, and the final order of depths must match the order of efficiencies strictly.
- Efficiencies were assumed to be distinct (a permutation), so "strictly increasing" is always reachable.
