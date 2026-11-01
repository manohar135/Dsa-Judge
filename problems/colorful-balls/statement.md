A shop has three types of single-colour balls: **X**, **Y** and **Z**, with $x$, $y$ and $z$ balls available. Any single ball can be sold on its own for $M$ rupees.

The shop can also combine balls into new coloured balls:

- **A** = one X + one Y, sells for $priceA$
- **B** = one Y + one Z, sells for $priceB$
- **C** = one X + one Y + one Z, sells for $priceC$

Each ball can be used only once: either sold as it is, or used in exactly one combo. Unused balls are sold at $M$ each.

Find the maximum money the shop can earn in a day.

### Input
A single line with seven integers: $x$, $y$, $z$, $M$, $priceA$, $priceB$, $priceC$.

### Output
Print a single integer: the maximum earning.

### Constraints
- $0 \le x, y, z \le 100$
- $0 \le M, priceA, priceB, priceC \le 1000$

### Explanation of Example 1
Make one C ($40$), then sell the remaining X and Z singly ($10 + 10$). Total $= 60$.

### Explanation of Example 2
Making combos earns less than selling the balls singly ($2 \times 50 = 100 > 60$ and $3 \times 50 = 150 > 100$), so sell all $9$ balls for $50$ each: $450$.
