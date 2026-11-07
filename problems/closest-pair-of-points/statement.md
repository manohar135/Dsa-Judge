Given `N` points on a 2D Cartesian plane, each with integer coordinates `(x_i, y_i)`, find the minimum **squared** Euclidean distance between any two distinct points (two different indices; their coordinates may coincide).

For two points `(x1, y1)` and `(x2, y2)` the squared distance is `(x1 − x2)² + (y1 − y2)²`. The square root is not required.

### Input
```
N
x_1 y_1
...
x_N y_N
```

### Output
A single integer: the minimum squared distance.

### Constraints
- 2 ≤ N ≤ 10^5
- −10^9 ≤ x_i, y_i ≤ 10^9
- The answer can be up to 8·10^18: use 64-bit integers (it still fits in a signed `long long`).

### Explanation of Example 1
(2,1) and (1,2): 1² + 1² = 2.

### Explanation of Example 2
Only one pair: 25 + 25.

### Explanation of Example 3
Two points share the same coordinates.
