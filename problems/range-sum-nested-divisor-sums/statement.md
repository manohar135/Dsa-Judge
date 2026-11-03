You are given two positive integers $L$ and $R$ ($1 \le L \le R$). Let us define two mathematical functions for any positive integer:

1. **$s(y)$ — Sum of Divisors of $y$:**
   $s(y)$ is the sum of all positive integers $d$ ($1 \le d \le y$) that evenly divide $y$:
   $$s(y) = \sum_{d \mid y} d$$
   *(For example, $s(4) = 1 + 2 + 4 = 7$, and $s(6) = 1 + 2 + 3 + 6 = 12$.)*

2. **$f(x)$ — Sum of $s(y)$ over all Divisors of $x$:**
   $f(x)$ is the sum of $s(y)$ for all positive integers $y$ ($1 \le y \le x$) such that $x \bmod y = 0$:
   $$f(x) = \sum_{y \mid x} s(y)$$
   *(For example, for $x = 4$, its divisors are $y \in \{1, 2, 4\}$, so $f(4) = s(1) + s(2) + s(4) = 1 + 3 + 7 = 11$.)*

Given $L$ and $R$, compute the total sum of $f(x)$ for all $x$ in the inclusive range $[L, R]$:
$$\text{Ans}(L, R) = \sum_{x = L}^{R} f(x)$$

### Input
A single line containing two space-separated integers $L$ and $R$.

### Output
Print a single 64-bit integer — the value of $\sum_{x = L}^{R} f(x)$.

### Constraints
- $1 \le L \le R \le 10^6$

### Explanation of Example 1
Divisor sums $s(y)$:
- $s(1) = 1$
- $s(2) = 1 + 2 = 3$
- $s(3) = 1 + 3 = 4$
- $s(4) = 1 + 2 + 4 = 7$

Values of $f(x)$ for $x \in [2, 4]$:
- $f(2) = s(1) + s(2) = 1 + 3 = 4$
- $f(3) = s(1) + s(3) = 1 + 4 = 5$
- $f(4) = s(1) + s(2) + s(4) = 1 + 3 + 7 = 11$

Total sum: $f(2) + f(3) + f(4) = 4 + 5 + 11 = 20$.

### Explanation of Example 2
For $x \in [1, 6]$, $f(1..6) = [1, 4, 5, 11, 7, 20]$, whose sum is $1 + 4 + 5 + 11 + 7 + 20 = 48$.

### Explanation of Example 3
For $L = R = 6$, the divisors of $6$ are $\{1, 2, 3, 6\}$, so $f(6) = s(1) + s(2) + s(3) + s(6) = 1 + 3 + 4 + 12 = 20$.

