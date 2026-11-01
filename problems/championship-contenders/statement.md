There are $n$ participants in a multi-stage tournament. Before the final race, the $i$-th participant has a score of $s_i$.

In the final race, points are awarded by finishing position:

- 1st place receives $n$ points,
- 2nd place receives $n - 1$ points,
- ...
- $n$-th (last) place receives $1$ point.

No two participants finish in the same position. A participant **wins** the tournament if their total score (initial score + points from the final race) is **greater than or equal to** the total score of every other participant.

Count the participants who have a theoretical chance of winning, i.e. for whom there exists at least one finishing order of the final race in which they achieve the maximum total score.

### Input
The first line contains a single integer $n$.

The second line contains $n$ integers $s_1, s_2, \dots, s_n$.

### Output
Print a single integer — the number of participants who can win.

### Constraints
- $1 \le n \le 10^5$
- $1 \le s_i \le 10^9$

### Explanation of Example 1
Points awarded are $[3, 2, 1]$.

- Participant 1 (score 8) finishes 1st, participant 3 finishes 2nd, participant 2 finishes 3rd: totals $[11, 11, 11]$. Participant 1 shares the maximum, so they can win.
- Participant 2 (score 10) finishes 1st and gets $13$, winning outright.
- Participant 3 (score 9) finishes 1st, participant 1 2nd, participant 2 3rd: totals $[10, 11, 12]$. Participant 3 wins.

All $3$ participants can win.
