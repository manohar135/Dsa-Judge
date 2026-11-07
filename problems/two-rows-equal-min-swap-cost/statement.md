You have two rows of `n` blocks each; `row1[i]` and `row2[i]` are block heights. You want every column to match: after rearranging, `row1[i] == row2[i]` for every `i`.

- Reordering blocks **inside one row** is free (you may permute each row any way you like).
- **Swapping** a block of `row1` with a block of `row2` costs `min(height1, height2)` of the two swapped blocks.

Return the minimum total cost to make the rows match, or `-1` if it's impossible.

### Input
```
n
row1[0] ... row1[n-1]
row2[0] ... row2[n-1]
```

### Output
A single integer: the minimum cost, or -1.

### Constraints
- 1 ≤ n ≤ 10^5
- 1 ≤ row1[i], row2[i] ≤ 10^9
- The answer can exceed 2^31 − 1: use 64-bit integers.

### Explanation of Example 1
Swap a 2 from row 1 with a 1 from row 2 (cost 1). Both rows become {1, 2, 2, 4}.

### Explanation of Example 2
4 and 5 each appear once in total, so they can never be matched.

### Explanation of Example 3
Already equal.
