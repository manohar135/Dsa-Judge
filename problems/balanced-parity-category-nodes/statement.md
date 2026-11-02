Flipkart's product catalogue is stored as a binary category tree. Each category has an `id` and a `value` (for example, the number of listed products), and an audit flags categories whose two sub-catalogues disagree in parity.

- You are given the `id` of the `root` node and an integer $n$ (the number of remaining nodes in the tree).
- Then $n$ lines follow, each of the form `path node`: `path` is a string over `L` / `R` describing the route from the root (e.g. `L`, `R`, `LL`, `LR`, `LRLR`), and `node` is the `id` of the node at that position.
- Node IDs are distinct positive integers, but need not be consecutive (e.g. `11`, `6`, `22`).
- You are also given an array `value` of $n + 1$ integers, where `value[i]` is the value of the $i$-th node (**root first**, then the $n$ nodes in input order).
- A node $u$ is **flagged** if it has **both** a left and a right child, and the sum of values in its left child's subtree and the sum of values in its right child's subtree have **different parity** (one odd, one even).

Find the sum of the IDs of all flagged nodes.

### Input
The first line contains two integers `root` and $n$ — the ID of the root node and the number of additional nodes.

The next $n$ lines each contain a string `path` (consisting of `'L'` and `'R'`) and an integer `node` — the path from the root and the ID of that node.

The last line contains $n + 1$ space-separated integers `value[0], value[1], ..., value[n]` — the values of the root followed by the $n$ nodes in the given input order.

### Output
Print a single integer — the sum of the IDs of all flagged nodes.

### Constraints
- $0 \le n \le 1000$
- $1 \le \text{node id} \le 10^6$ (all node IDs are distinct)
- $0 \le \text{value}[i] \le 10^9$
- The given paths always form a valid binary tree rooted at `root`.

### Explanation of Example 1
Nodes in input order are $(11, 6, 22, 4, 9)$ with values $[3, 1, 2, 4, 6]$:
- **Node 6** (`L`): left subtree $\{4\}$ has sum $4$ (even), right subtree $\{9\}$ has sum $6$ (even) $\to$ same parity, not flagged.
- **Node 11** (root): left subtree $\{6, 4, 9\}$ has sum $1 + 4 + 6 = 11$ (odd), right subtree $\{22\}$ has sum $2$ (even) $\to$ different parity, **flagged**.

Sum of flagged node IDs $= 11$.

### Explanation of Example 2
Nodes in input order are $(10, 3, 25, 7, 14, 2, 30)$ with values $[1, 2, 3, 4, 5, 6, 7]$:
- **Node 3** (`L`): left sum $4$ vs right sum $5$ $\to$ **flagged**.
- **Node 25** (`R`): left sum $6$ vs right sum $7$ $\to$ **flagged**.
- **Node 10** (root): left sum $2 + 4 + 5 = 11$ vs right sum $3 + 6 + 7 = 16$ $\to$ **flagged**.

Sum of flagged node IDs $= 10 + 3 + 25 = 38$.

### Explanation of Example 3
No node has both a left and a right child, so the answer is $0$.

