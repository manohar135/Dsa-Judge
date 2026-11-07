A neural network has `n` layers. Layer `i` (0-indexed) starts at depth `i + 1`, has an efficiency `efficiency[i]` (all efficiencies are distinct, a permutation of 1..n) and an increment `incr[i]`.

In one operation you pick a layer `i` and increase its depth by `incr[i]`. Depths can only increase.

Find the minimum number of operations so that when the layers are ordered by depth, their efficiencies are **strictly increasing**. In other words, for every two layers, the one with the lower efficiency must end up at a strictly smaller depth.

### Input
```
n
efficiency[0] ... efficiency[n-1]
incr[0] ... incr[n-1]
```

### Output
A single integer: the minimum number of operations.

### Constraints
- 1 ≤ n ≤ 10^5
- `efficiency` is a permutation of 1..n
- 1 ≤ incr[i] ≤ 10^4
- The answer can reach about 5·10^9: use 64-bit integers.

### Explanation of Example 1
Layers at depths 1, 2, 3 have efficiencies 3, 1, 2. The efficiency-3 layer must go below depth 3: three operations take it to depth 4.

### Explanation of Example 2
The efficiency-1 layer is at depth 2, so the efficiency-2 layer (depth 1, incr 1) must reach depth 3: two operations.

### Explanation of Example 3
Already in order.
