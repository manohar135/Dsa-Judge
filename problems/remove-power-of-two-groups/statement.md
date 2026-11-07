You are given an array `w` of `n` exponents; element `i` has weight `2^w[i]`.

In one step you may choose any non-empty set of the remaining elements whose total weight is a power of two, i.e. `2^{w[i1]} + 2^{w[i2]} + ... + 2^{w[im]} = 2^p` for some integer `p ≥ 0`, and remove them all.

Return the minimum number of steps needed to remove every element.

### Input
```
n
w[0] w[1] ... w[n-1]
```

### Output
A single integer: the minimum number of steps.

### Constraints
- 1 ≤ n ≤ 3·10^5
- 0 ≤ w[i] ≤ 10^6 (weights are far too large to store directly)

### Explanation of Example 1
Remove {1, 1, 2, 3} (2 + 2 + 4 + 8 = 16 = 2^4), then {3} (8 = 2^3).

### Explanation of Example 2
1, 2, 4 and 8 can't be grouped into a power of two in any way, so each needs its own step.

### Explanation of Example 3
All exponents differ, so every element must go alone.
