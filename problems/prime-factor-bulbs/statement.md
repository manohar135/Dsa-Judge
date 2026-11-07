You are given a list of `numbers` and a binary array `bulbs` of length `n`, where `bulbs[i] = 1` means bulb `i + 1` is on and `0` means it is off (bulbs are numbered 1..n).

Process the numbers in order. For each number, find its **distinct** prime factors; for every such prime `p`, toggle bulb `p` (on ↔ off). Primes larger than `n` have no bulb and are ignored.

Return the final state of all bulbs.

### Input
```
n q
bulbs[0] ... bulbs[n-1]
numbers[0] ... numbers[q-1]
```

### Output
`n` values (one per line): the final state of bulbs 1..n.

### Constraints
- 1 ≤ n ≤ 10^5, 1 ≤ q ≤ 10^5
- bulbs[i] ∈ {0, 1}
- 1 ≤ numbers[i] ≤ 10^6

### Explanation of Example 1
12 = 2²·3 toggles bulbs 2 and 3; 5 toggles bulb 5.

### Explanation of Example 2
8 toggles bulb 2, 9 toggles bulb 3, 6 toggles 2 and 3 again: all back on.

### Explanation of Example 3
1 has no prime factors; 7 > 3 has no bulb.
