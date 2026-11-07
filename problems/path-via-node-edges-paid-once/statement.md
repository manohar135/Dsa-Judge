You are given a weighted undirected graph with `n` nodes (numbered 1..n) and `m` edges, and three nodes `a`, `b`, `c`.

You must walk from `a` to `b`, visiting `c` somewhere on the way. You may traverse any edge any number of times, but **each edge's weight is paid only the first time** you use it.

Return the minimum total cost, or `-1` if no such walk exists.

### Input
```
n m
a b c
u_1 v_1 w_1
...
u_m v_m w_m
```

### Output
A single integer: the minimum cost, or -1.

### Constraints
- 1 ≤ n ≤ 10^5, 0 ≤ m ≤ 2·10^5
- 1 ≤ u_i, v_i ≤ n, u_i ≠ v_i (parallel edges are allowed)
- 1 ≤ w_i ≤ 10^9
- 1 ≤ a, b, c ≤ n (they need not be distinct)
- The answer can exceed 2^31 − 1: use 64-bit integers.

### Explanation of Example 1
Walk 1 → 2 → 3 → 2 → 4. Edge 2–3 is used twice but paid once: 2 + 3 + 4 = 9.

### Explanation of Example 2
Walk 1 → 3 → 4 → 3 → 2 pays 1 + 10 + 1 = 12, cheaper than using the edge 1–2 (5).

### Explanation of Example 3
Node 3 can't be reached.
