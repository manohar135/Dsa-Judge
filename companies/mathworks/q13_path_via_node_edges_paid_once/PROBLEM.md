# Q13. Shortest Route Through a Checkpoint, Edges Paid Once

Run: `python driver.py -13`  ·  Edit: `solution.cpp` in this folder
Category: Graphs / Dijkstra  ·  Source: MathWorks Q1 ("min dist to go from a to b via c, if I traverse an edge once its weight is not counted next time")

## Problem Description

You are given a weighted undirected graph with `n` nodes (numbered 1..n) and `m` edges, and three nodes `a`, `b`, `c`.

You must walk from `a` to `b`, visiting `c` somewhere on the way. You may traverse any edge any number of times, but **each edge's weight is paid only the first time** you use it.

Return the minimum total cost, or `-1` if no such walk exists.

## Function signature

```cpp
// n : nodes 1..n, edges[i] = {u, v, w} undirected
// a, b, c : go from a to b passing through c; an edge's weight is paid only once
// Return the minimum total cost, or -1 if impossible (64-bit).
long long minCostVia(int n, vector<vector<int>>& edges, int a, int b, int c);
```

## Input Format

```
n m
a b c
u_1 v_1 w_1
...
u_m v_m w_m
```

## Output Format

A single integer: the minimum cost, or -1.

## Constraints

- 1 ≤ n ≤ 10^5, 0 ≤ m ≤ 2·10^5
- 1 ≤ u_i, v_i ≤ n, u_i ≠ v_i (parallel edges are allowed)
- 1 ≤ w_i ≤ 10^9
- 1 ≤ a, b, c ≤ n (they need not be distinct)
- The answer can exceed 2^31 − 1: use 64-bit integers.

## Example 1

Input:
```
4 3
1 4 3
1 2 2
2 3 3
2 4 4
```
Output:
```
9
```
Explanation: Walk 1 → 2 → 3 → 2 → 4. Edge 2–3 is used twice but paid once: 2 + 3 + 4 = 9.

## Example 2

Input:
```
4 4
1 2 4
1 2 5
2 3 1
1 3 1
3 4 10
```
Output:
```
12
```
Explanation: Walk 1 → 3 → 4 → 3 → 2 pays 1 + 10 + 1 = 12, cheaper than using the edge 1–2 (5).

## Example 3

Input:
```
3 1
1 2 3
1 2 7
```
Output:
```
-1
```
Explanation: Node 3 can't be reached.

## Notes / Assumptions

- Input order: `n m` on the first line, then `a b c`, then the edges.
