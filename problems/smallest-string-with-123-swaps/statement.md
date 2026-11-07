You are given a string `S` of digits `1`, `2` and `3`. You may repeatedly apply two kinds of adjacent swaps:

- `"21"` becomes `"12"`
- `"32"` becomes `"23"`

No other swap is allowed (in particular, adjacent `1` and `3` may never be swapped, and the swaps never go the other way).

Return the lexicographically smallest string that can be reached.

### Input
```
S
```

### Output
The smallest reachable string.

### Constraints
- 1 ≤ |S| ≤ 10^5
- `S` consists only of `1`, `2`, `3`.

### Explanation of Example 1
"32" → "23" gives 231. No more swaps apply.

### Explanation of Example 2
2213 → 2123 → 1223.

### Explanation of Example 3
No "21" or "32" pair exists, so nothing can move.
