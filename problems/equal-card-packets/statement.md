You are given an array `cards` of size $n$, where `cards[i]` represents the frequency of the $i$-th card type.

You need to divide all cards into `packets` ($> 1$) identical packets such that **every packet has an equal number of cards of each type**.

Return the **minimum total number of cards you must add** so that dividing the cards into $p > 1$ identical packets becomes possible.

### Input
- The first line contains an integer $n$ — the number of card types.
- The second line contains $n$ space-separated integers `cards[0], cards[1], ..., cards[n - 1]`.

### Output
Print a single integer — the minimum number of cards to add.

### Constraints
- $1 \le n \le 1000$
- $1 \le \text{cards}[i] \le 1000$

### Explanation of Example 1
`cards = [2, 4, 8]`
- We can form $2$ packets: `(1, 2, 4)` and `(1, 2, 4)` with `0` cards added.

### Explanation of Example 2
`cards = [3, 11]`
- Add `1` card of the second type (`11 -> 12`) to get `[3, 12]`.
- We can then form $3$ identical packets: `(1, 4)`, `(1, 4)`, `(1, 4)`.
- Minimum cards added $= 1$.

### Explanation of Example 3
`cards = [5, 7, 11]`
- Forming $2$ packets requires adding $1$ card of each type (`[6, 8, 12]`), which adds $1 + 1 + 1 = 3$ cards.

