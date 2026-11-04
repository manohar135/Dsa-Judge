You are given an array `arr` of size $n$. In each iteration, you must:

1. Find the **minimum element** in the current array (if there is a tie, choose the **leftmost** occurrence).
2. Add this minimum element to the total sum.
3. **Delete** the minimum element along with its immediate left and right neighbours in the current array, if they exist.
4. Repeat the process on the remaining array until it becomes empty.

Return the sum of all the minimum elements selected across all iterations.

### Input
- The first line contains an integer $n$ — the size of the array.
- The second line contains $n$ space-separated integers `arr[0], arr[1], ..., arr[n - 1]`.

### Output
Print a single integer — the sum of all minimum elements selected across all iterations.

### Constraints
- $1 \le n \le 5000$
- $-10^9 \le \text{arr}[i] \le 10^9$

### Explanation of Example 1
- **Iteration 1:** The minimum element in `[2, 1, 3, 4, 5]` is `1`. Remove `1` and its adjacent elements `2` and `3`. The remaining array is `[4, 5]`. Sum $= 1$.
- **Iteration 2:** The minimum element in `[4, 5]` is `4`. Remove `4` and its adjacent element `5`. The array becomes empty. Sum $= 1 + 4 = 5$.

### Explanation of Example 2
- **Iteration 1:** The minimum element in `[10, 4, 1, 5, 20]` is `1`. Removing `4, 1, 5` leaves the remaining array `[10, 20]`. Sum $= 1$.
- **Iteration 2:** In the remaining array `[10, 20]`, the minimum element is `10`, and `20` is now its immediate right neighbour, so both are removed. Sum $= 1 + 10 = 11$.

### Explanation of Example 3
- **Iteration 1:** In `[3, 1, 1, 2]`, the leftmost minimum is the first `1` (at index $1$). Removing `3, 1, 1` leaves `[2]`. Sum $= 1$.
- **Iteration 2:** Remove `2`. Sum $= 1 + 2 = 3$.

