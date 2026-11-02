Mona is an on-site service engineer for a laptop manufacturer. She regularly travels across her territory visiting the sites where laptop servicing needs to be done. She works **8 hours a day**, spending time either travelling to a site or providing service at the site.

You are given information about Mona's territory in the form of an $R \times C$ dimensional array $matrix$. Each cell in the $matrix$ contains a number denoting the time needed by Mona to complete the servicing at that site. In case a cell has $0$, it means that no servicing is required there.

Mona can move only horizontally or vertically at a time and she takes **2 hours** to move to the next cell.

Mona starts at cell $(0, 0)$ and can finish in any cell. Your job is to find the minimum number of days in which she can complete all the tasks.

### Input
The first line contains two integers $R$ and $C$ — denoting the number of rows and columns in $matrix$.

The next $R$ lines contain $C$ integers each — denoting the cells of $matrix$.

### Output
Print the minimum number of days in which Mona can complete all the tasks.

### Constraints
- $1 \le R \le 30$
- $1 \le C \le 30$
- $0 \le matrix[i][j] \le 1000$
- It's guaranteed the number of non-zero cells in $matrix \le 15$.

### Explanation of Example 1
Servicing takes $2 + 1 = 3$ hours; route $(0,0) \to (2,2)$ covers $4$ units $= 8$ hours; total $11$ hours $\to 2$ days.

### Explanation of Example 2
Servicing takes $3 + 3 + 5 = 11$ hours; route $(0,0) \to (1,0) \to (2,2)$ covers $4$ units $= 8$ hours; total $19$ hours $\to 3$ days.

### Explanation of Example 3
No servicing is required, so $0$ days are needed.
