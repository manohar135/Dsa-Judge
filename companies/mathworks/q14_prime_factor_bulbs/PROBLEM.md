# Q14. Prime Factor Bulbs

Run: `python driver.py -14`  ·  Edit: `solution.cpp` in this folder
Category: Number theory / Sieve  ·  Source: MathWorks Q2 ("find their prime factors... bulbs[i] = 1 means on... for each prime factor change that bulb's state")

## Problem Description

You are given a list of `numbers` and a binary array `bulbs` of length `n`, where `bulbs[i] = 1` means bulb `i + 1` is on and `0` means it is off (bulbs are numbered 1..n).

Process the numbers in order. For each number, find its **distinct** prime factors; for every such prime `p`, toggle bulb `p` (on ↔ off). Primes larger than `n` have no bulb and are ignored.

Return the final state of all bulbs.

## Function signature

```cpp
// bulbs : bulbs[i] is the state of bulb i+1 (1 = on)
// numbers : for each number, every distinct prime factor p toggles bulb p (if p <= n)
// Return the final bulb states.
vector<int> finalBulbStates(vector<int>& bulbs, vector<int>& numbers);
```

## Input Format

```
n q
bulbs[0] ... bulbs[n-1]
numbers[0] ... numbers[q-1]
```

## Output Format

`n` values (one per line): the final state of bulbs 1..n.

## Constraints

- 1 ≤ n ≤ 10^5, 1 ≤ q ≤ 10^5
- bulbs[i] ∈ {0, 1}
- 1 ≤ numbers[i] ≤ 10^6

## Example 1

Input:
```
6 2
0 0 0 0 0 0
12 5
```
Output:
```
0 1 1 0 1 0
```
Explanation: 12 = 2²·3 toggles bulbs 2 and 3; 5 toggles bulb 5.

## Example 2

Input:
```
5 3
1 1 1 1 1
8 9 6
```
Output:
```
1 1 1 1 1
```
Explanation: 8 toggles bulb 2, 9 toggles bulb 3, 6 toggles 2 and 3 again: all back on.

## Example 3

Input:
```
3 2
1 0 1
1 7
```
Output:
```
1 0 1
```
Explanation: 1 has no prime factors; 7 > 3 has no bulb.

## Notes / Assumptions

- The recollection was short. Assumptions: bulbs are **1-indexed** by the prime itself, each number toggles each of its **distinct** primes once (12 toggles bulb 2 once, not twice), and primes > n are ignored. Another plausible reading is "toggle every bulb whose index is a multiple of p"; tell me if your OA was that one.
