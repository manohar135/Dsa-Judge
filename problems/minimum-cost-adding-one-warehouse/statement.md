You are given a grid of size $N \times M$ containing only `0`s and `1`s. A cell with value `1` represents a cell that already has an Amazon warehouse; a cell with value `0` has none. It is guaranteed that at least one `1` and at least one `0` exist.

For any cell $(i, j)$, define its **cost** as the Chebyshev ($L_\infty$) distance to the nearest warehouse:
$$\text{cost}(i, j) = \min_{(u, v) \in \text{warehouses}} \max(|i - u|, |j - v|)$$
*(A warehouse cell itself has cost $0$.)*

Define the **total cost** of the grid as the sum of $\text{cost}(i, j)$ over every cell in the grid.

You are allowed to convert **exactly one** `0`-cell into a `1` (build one new warehouse at an empty cell). Choose the cell that minimizes the resulting total cost, and return that minimum total cost.

### Input
- The first line contains two space-separated integers $N$ and $M$ — the number of rows and columns.
- Each of the next $N$ lines contains $M$ space-separated integers (`0` or `1`) representing the grid.

### Output
Print a single integer — the minimum total cost of the grid achievable after adding exactly one new warehouse.

### Constraints
- $1 \le N, M \le 500$
- Grid values are only `0` or `1`, with at least one `1` and at least one `0`.

### Explanation of Example 1
In the $4 \times 4$ grid with a single warehouse at $(3, 3)$, the initial total cost is $34$. Building the new warehouse at $(1, 1)$ reduces the costs of cells in the upper-left region so that the new grid costs sum to $18$, which is optimal.

### Explanation of Example 2
All four corners have warehouses, so all five `0`-cells initially have cost $1$ (total $5$). Adding a warehouse at any `0`-cell sets that cell's cost to $0$, lowering the total cost to $4$.

### Explanation of Example 3
In `1 0 0 0 0`, placing the new warehouse at index $3$ (`1 0 0 1 0`) makes the cell costs `[0, 1, 1, 0, 1]`, whose sum is $3$.

