You are given a string `key` of length $n$ consisting of lowercase English letters. You want to construct a new string called `identifier` (initially empty) by maintaining an active subarray $[l, r]$, initialized to $l = 0$ and $r = n - 1$.

In each step, while $l \le r$:

1. Choose any index $i$ within the current active range ($l \le i \le r$).
2. Append the character `key[i]` to the end of `identifier`.
3. Discard `key[i]` along with one of the two sides around $i$, and keep the other side as the new active range:
   - Either keep the **left** subarray by setting $r = i - 1$ (discarding $[i, r]$),
   - Or keep the **right** subarray by setting $l = i + 1$ (discarding $[l, i]$).
4. Repeat this process until the active range becomes empty ($l > r$).

Return the **lexicographically largest** `identifier` that can be generated.

### Input
A single line containing the string `key` of lowercase English letters (`'a'`–`'z'`).

### Output
Print a single line — the lexicographically largest `identifier` that can be generated.

### Constraints
- $1 \le n \le 10^5$
- `key` consists only of lowercase English letters (`'a'`–`'z'`).

### Explanation of Example 1
Initially, $l = 0, r = 4$ (`"adcdb"`), and `identifier = ""`.
- **Step 1:** The largest character in `"adcdb"` is `'d'`, appearing at indices $1$ and $3$. Pick $i = 1$ (`'d'`) and keep the right subarray $[2, 4]$ (`"cdb"`). `identifier = "d"`.
- **Step 2:** In `"cdb"` ($[2, 4]$), pick $i = 3$ (`'d'`). The left side $[2, 2]$ is `"c"` and the right side $[4, 4]$ is `"b"`. Since `'c' > 'b'`, keep the left subarray $[2, 2]$. `identifier = "dd"`.
- **Step 3:** In `"c"` ($[2, 2]$), pick $i = 2$ (`'c'`). The range becomes empty ($l > r$). `identifier = "ddc"`.

### Explanation of Example 2
For `key = "abacaba"`, picking all four `'a'`s is worse than starting with `'c'` at index $3$; after picking `'c'`, both sides $[0, 2]$ and $[4, 6]$ are `"aba"`, from which we pick `'b'` and then `'a'`, giving `"cba"`.

### Explanation of Example 3
For `key = "zazbz"`, we pick all three `'z'` characters by peeling from the ends, leaving `"b"` between the second and third `'z'`, yielding `"zzzb"`.

