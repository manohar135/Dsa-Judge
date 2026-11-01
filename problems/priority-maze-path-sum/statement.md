You are given a grid $maze$ with $R$ rows and $C$ columns of non-negative integers. You start at the top-left cell $(0, 0)$ and want to reach the bottom-right cell $(R-1, C-1)$.

Movement rules:

1. **Valid moves:** from $(r, c)$ you may only move **Down** to $(r+1, c)$ or **Right** to $(r, c+1)$.
2. **Blocked cells:** a cell containing $0$ is an obstacle and cannot be visited.
3. **Direction priority:** if both Down and Right can lead to the destination, you must take **Down**. If moving Down leads into a dead end, backtrack and take Right instead.

Equivalently, among all valid paths from the start to the destination, take the one found first when exploring Down before Right.

Print the sum of all values on that path (including the start and the destination). If no valid path exists, print $-1$.

### Input
The first line contains two integers $R$ and $C$.

Each of the next $R$ lines contains $C$ integers: the values of $maze$.

### Output
Print a single integer: the sum of the chosen path, or $-1$ if there is none.

### Constraints
- $1 \le R, C \le 1000$
- $0 \le maze[r][c] \le 10^5$

### Explanation of Example 1
Start at $(0,0)$ with value $2$. Both Down $(1,0)$ and Right $(0,1)$ are open, so go Down. At $(1,0)$ Down is blocked, so go Right to $(1,1)$. There Down $(2,1)$ is open and Right is blocked, so go Down, then Right to the destination. The path is $2 \to 3 \to 4 \to 6 \to 2$, with sum $17$.

### Explanation of Example 2
Going Down from $(0,0)$ to $(1,0)$ is a dead end, so backtrack and go Right: $1 \to 2 \to 3 \to 5 \to 6$, with sum $17$.
