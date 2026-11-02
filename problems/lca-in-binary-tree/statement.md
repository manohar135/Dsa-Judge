Consider a binary tree with $N$ nodes: one root and $N - 1$ descendants. Each descendant node is represented by its relationship to the root using a string containing `L` and `R`:

- `L`: left child of the root.
- `R`: right child of the root.
- `LL`: left child of the node at path `L`.
- `LR`: right child of the node at path `L`, and so on.

Given two node values $A$ and $B$, find their **Lowest Common Ancestor (LCA)**.

The LCA is the deepest node that is an ancestor of both nodes. A node is considered an ancestor of itself.

### Input
- First line: An integer $N$, the total number of nodes in the binary tree.
- Second line: An integer `Root`, the value of the root node.
- Next $N - 1$ lines: A string $S$ (over `L` and `R`) and an integer $X$, representing the path of node $X$ from the root.
- Last line: Two space-separated integers $A$ and $B$, whose LCA must be found.

### Output
Print a single integer — the value of the Lowest Common Ancestor of nodes $A$ and $B$.

### Constraints
- $1 \le N \le 2000$
- $1 \le \text{node value} \le 10^9$ (all node values are distinct)
- The given paths always form a valid binary tree rooted at `Root`.
- $A$ and $B$ are guaranteed to be present in the tree.

### Explanation of Example 1
- Node `4` has path `LL`.
- Node `5` has path `LR`.
- Their paths share the longest common prefix `L`, which represents node `2`.
- Therefore, the Lowest Common Ancestor is `2`.

### Explanation of Example 2
- Node `20` has path `L` and node `60` has path `LRL`.
- Since node `20` lies on the path to node `60` (and a node is an ancestor of itself), their LCA is `20`.

### Explanation of Example 3
- Node `12` (`LR`) is in the left subtree of the root and node `15` (`RL`) is in the right subtree of the root, so their LCA is the root `7`.

