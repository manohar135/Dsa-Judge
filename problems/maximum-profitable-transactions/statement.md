You are given an array of $n$ integers `transactions`, where each integer denotes the profit (positive) or loss (negative) of a transaction.

You can select **any subset** of transactions (and process them in an optimal order) as long as your **net profit remains strictly positive** ($> 0$).

Return the **maximum number of transactions** you can take.

### Input
- The first line contains an integer $n$ — the number of transactions.
- The second line contains $n$ space-separated integers `transactions[0], ..., transactions[n - 1]`.

### Output
Print a single integer — the maximum number of transactions you can select such that the net profit is strictly positive ($> 0$), or `0` if no such selection exists.

### Constraints
- $1 \le n \le 10^5$
- $-10^9 \le \text{transactions}[i] \le 10^9$

### Explanation of Example 1
Transactions: `[4, -2, -1, 3, -5]`
- Take all positive transactions first: `4 + 3 = 7` ($2$ transactions).
- Add the smallest losses while net profit stays $> 0$:
  - Add `-1` $\to$ net profit $= 6 > 0$ ($3$ transactions).
  - Add `-2` $\to$ net profit $= 4 > 0$ ($4$ transactions).
  - Adding `-5` would make net profit $-1 \le 0$, so we stop.
- Maximum transactions $= 4$.

### Explanation of Example 2
Transactions: `[-3, 0, -1, -5]`
- No transaction has a positive profit, so it is impossible to achieve a net profit $> 0$. Answer is `0`.

### Explanation of Example 3
Transactions: `[2, 0, 0, -1, -2]`
- Take `2`, both `0`s, and `-1` for a net profit of $2 + 0 + 0 - 1 = 1 > 0$ ($4$ transactions).

