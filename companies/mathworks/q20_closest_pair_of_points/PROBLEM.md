# Q20. Closest Pair of Points

Run: `python driver.py -20`  ·  Edit: `solution.cpp` in this folder
Category: Geometry / Sweep line / Divide and conquer  ·  Source: MathWorks CS OA PDF, problem 1 (also IIITH compendium, 4.1)

## Problem Description

Given `N` points on a 2D Cartesian plane, each with integer coordinates `(x_i, y_i)`, find the minimum **squared** Euclidean distance between any two distinct points (two different indices; their coordinates may coincide).

For two points `(x1, y1)` and `(x2, y2)` the squared distance is `(x1 − x2)² + (y1 − y2)²`. The square root is not required.

## Function signature

```cpp
// points : points[i] = {x, y}
// Return the minimum squared Euclidean distance between two different points (64-bit).
long long closestPairSquared(vector<vector<int>>& points);
```

## Input Format

```
N
x_1 y_1
...
x_N y_N
```

## Output Format

A single integer: the minimum squared distance.

## Constraints

- 2 ≤ N ≤ 10^5
- −10^9 ≤ x_i, y_i ≤ 10^9
- The answer can be up to 8·10^18: use 64-bit integers (it still fits in a signed `long long`).

## Example 1

Input:
```
4
2 1
4 4
1 2
6 3
```
Output:
```
2
```
Explanation: (2,1) and (1,2): 1² + 1² = 2.

## Example 2

Input:
```
2
0 0
5 5
```
Output:
```
50
```
Explanation: Only one pair: 25 + 25.

## Example 3

Input:
```
3
1 1
3 3
1 1
```
Output:
```
0
```
Explanation: Two points share the same coordinates.

## Notes / Assumptions

- Same task as CSES 2194 (Minimum Euclidean Distance). The O(N²) all-pairs check times out.
