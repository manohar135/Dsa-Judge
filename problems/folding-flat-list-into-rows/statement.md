A report arrives as one flat list of integers `vec`. Its first entry is not data: `vec[0]` tells you how many **columns** the table should have. Every entry after it is a table value, listed in reading order — the first row from left to right, then the second row, and so on.

Rebuild the table. With $c = \text{vec}[0]$ columns, row $1$ holds $\text{vec}[1], \dots, \text{vec}[c]$, row $2$ holds $\text{vec}[c + 1], \dots, \text{vec}[2c]$, and so on until every value has been placed. The number of values after the first entry is always a positive multiple of $c$, so every row comes out full.

### Input
- The first line contains $L$, the length of `vec`.
- The second line contains the $L$ space-separated integers `vec[0], vec[1], ..., vec[L - 1]`.

### Output
Print the table one row per line, top row first, with the values of a row separated by single spaces.

### Constraints
- $2 \le L \le 1501$
- $1 \le \text{vec}[0] \le L - 1$, and $L - 1$ is a multiple of $\text{vec}[0]$
- $-100000 \le \text{vec}[i] \le 100000$ for $i \ge 1$

### Explanation of Example 1
`vec[0] = 2`, so the six values `4 5 8 9 10 15` are cut into rows of two.

### Explanation of Example 2
Three columns (`vec[0] = 3`), so the six values form two rows of three. Values are copied as they are, including negatives and repeats.

### Explanation of Example 3
With a single column (`vec[0] = 1`), every value sits on its own row.

