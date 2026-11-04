A test rig produces a batch of $N$ positive whole-number readings, `values[0] ... values[N-1]`. For each reading, the analysis team needs its **divisor total**: the sum of every positive whole number that divides the reading with no remainder.

A divisor list always contains `1` and the reading itself. For instance, `18` is divided exactly by `1, 2, 3, 6, 9` and `18`, so its divisor total is `39`.

Complete the function `divisorSums(n, values)`, which returns a list of $N$ numbers whose $i$-th entry is the divisor total of `values[i]`.

Things to keep in mind:
- Both `1` and the reading itself are counted. The divisor total of `1` is `1`, and the divisor total of a prime $p$ is $p + 1$.
- Each divisor is added once. For a perfect square such as `49 = 7 * 7`, the divisor `7` is counted one time.
- Report the totals in the same order as the readings. A reading that repeats gets its total repeated.
- A divisor total can be more than twice the reading and exceeds $2^{31} - 1$ for some readings near $10^9$, so store the totals in a 64-bit integer type.
- Readings reach $10^9$, so trying every number from `1` up to the reading is far too slow.

### Input
- The first line holds one integer $N$.
- The second line holds $N$ integers `values[0] ... values[N-1]`, separated by single spaces.

### Output
Print the $N$ divisor totals on one line, in input order, separated by single spaces.

### Constraints
- $1 \le N \le 1000$
- $1 \le \text{values}[i] \le 10^9$

### Explanation of Example 1
`6` has divisors `1, 2, 3, 6` (total `12`). `1` has the single divisor `1`. `9` has divisors `1, 3, 9`, with `3` counted once (total `13`). `13` is prime, so its total is `1 + 13 = 14`.

### Explanation of Example 2
`28` has divisors `1, 2, 4, 7, 14, 28`, which add up to `56`; it appears twice, so `56` is printed twice, in place. `12` has divisors `1, 2, 3, 4, 6, 12`, which add up to `28`.

### Explanation of Example 3
$10^9 = 2^9 \cdot 5^9$, and its divisor total `2497558338` is larger than $2^{31} - 1$. `999999937` is prime, so its total is `999999938`.

