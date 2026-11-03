A college library keeps a small **reading desk** next to the counter so that popular books do not have to be fetched from the basement stacks every time. The desk can hold at most $c$ books, and every book takes exactly one place on it.

During the day, $n$ borrowers ask for books one after another; `codes[i]` is the catalogue code of the book asked for by the $i$-th borrower. Each request is handled as follows:

- If the book is already on the desk, the request is **served from the desk**. The book stays on the desk and now counts as the one handled most recently.
- Otherwise the book is brought up from the stacks and put on the desk. If the desk already holds $c$ books, the book whose last request is the **oldest** is first sent back to the stacks to make room.

The desk starts empty. The librarian wants at least $k$ of the $n$ requests to be served from the desk. Complete the logic for `minimumDeskCapacity(codes, k)`, which returns the smallest desk capacity $c$ ($c \ge 1$) for which this happens, or `-1` if no capacity at all achieves it.

### Input
- Line 1: the number of requests $n$.
- The next $n$ lines: one catalogue code per line, in the order the requests arrive.
- Last line: the target $k$.

### Output
One integer: the smallest capacity that serves at least $k$ requests from the desk, or `-1`.

### Constraints
- $1 \le k \le n \le 20000$
- Every catalogue code has $1$ to $8$ characters, each a lowercase English letter or a digit.

### Explanation of Example 1
With room for $2$ books only the third request (`m7`) is served from the desk; when `x9` arrives the desk holds `q2` and `m7`, `q2` was handled longest ago and goes back, and later `q2` and `m7` both have to be fetched again. With room for $3$ books nothing is ever sent back, and the requests at positions $3$, $5$ and $6$ are served from the desk. So $3$ is the smallest capacity giving at least $2$.

### Explanation of Example 2
The only repeated book, `ab`, is asked for again after two other books. A desk of $2$ has already sent `ab` back by then; a desk of $3$ still has it.

### Explanation of Example 3
Every book is requested once, so no request can ever be served from the desk, whatever its size.

