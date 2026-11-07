You are given the busy intervals of a group of people, all merged into one list: `busy[i] = [start_i, end_i]` means *someone* is busy during the half-open time range `[start_i, end_i)`. Time starts at 0. Intervals may overlap, nest or touch, and are given in any order.

Find the earliest time `t ≥ 0` such that **nobody** is busy at any moment of `[t, t + k)`.

### Input
```
n k
start_0 end_0
...
start_{n-1} end_{n-1}
```

### Output
A single integer: the earliest valid start time `t`.

### Constraints
- 1 ≤ n ≤ 10^5
- 1 ≤ k ≤ 10^9
- 0 ≤ start_i < end_i ≤ 10^9
- The answer is at most 10^9 (it always exists, since time is unbounded after the last meeting).

### Explanation of Example 1
Free gaps: [0,1) (too short) and [5,8) (length 3). So t = 5.

### Explanation of Example 2
The gap [2,3) is only 1 long; after time 4 everyone is free.

### Explanation of Example 3
[0,4) is free.
