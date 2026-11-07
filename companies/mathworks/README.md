# MathWorks OA practice kit

LeetCode-style C++ judge for 23 coding problems collected from MathWorks online assessments
(WhatsApp recollections, the IIITH 2026 compendium, the CS OA write-up and screenshots).
The aptitude MCQs from the screenshots are in [APTITUDE.md](APTITUDE.md).

Format of the real test, as reported: **3 coding questions + 5 aptitude MCQs, about 90 minutes**,
and different candidates got different sets. So pick 3 questions at random and give yourself 75 minutes.

## Questions

| Flag | Folder | Title | Source |
|---|---|---|---|
| `-1` | `q1_least_unique_after_k_removals/` | Least Number of Unique Integers after K Removals | WhatsApp list: "Leetcode 1481" |
| `-2` | `q2_min_groups_valid_assignment/` | Minimum Number of Groups to Create a Valid Assignment | WhatsApp list: "Leetcode 2910" |
| `-3` | `q3_sum_of_divisors/` | Sum of Divisors of Every Element | WhatsApp list: "1. Find sum of factors for all elements in given array" |
| `-4` | `q4_max_sum_fixed_length_pieces/` | Maximum Sum of Fixed-Length Pieces | WhatsApp list: "2. We can take subarray of length 1 x times, 2 y times and length 3 z times ... largest sum ... should not overlap" |
| `-5` | `q5_hamming_consecutive_windows/` | Hamming Distance of Consecutive Windows | WhatsApp list: "Hamming distance of consecutive substrings of length k over a string s" (also in the IIITH compendium, 4.4) |
| `-6` | `q6_merge_strings_min_inversions/` | Merge Two Strings with Minimum Inversions | WhatsApp list: "merge 2 strings such that both relative order preserved but min inversion count" (also IIITH compendium, 4.5) |
| `-7` | `q7_earliest_common_free_slot/` | Earliest Common Free Slot | WhatsApp list: "intervals where people are busy... find min starting time where people can be free for k hrs" (also IIITH compendium, 4.6) |
| `-8` | `q8_remove_power_of_two_groups/` | Remove Power-of-Two Groups | WhatsApp list: "we can select any numbers... 2^2 + 2^4 + 2^5 should be 2^p then we can remove them, min steps to empty the array" (also IIITH compendium, 4.7) |
| `-9` | `q9_two_rows_equal_min_swap_cost/` | Make Two Rows Equal with Minimum Swap Cost | WhatsApp list: "two rows... make each number in opposite direction have the same height... swap in same row no cost, between rows has cost... min, else -1" (also IIITH compendium, 4.8) |
| `-10` | `q10_min_subsequences_with_majority/` | Minimum Subsequences with a Majority Element | MathWorks (IITB) Question 1 |
| `-11` | `q11_scatter_palindrome_substrings/` | Scatter Palindrome Substrings | MathWorks (IITB) Question 2, and the MathWorks CS OA PDF, problem 2 |
| `-12` | `q12_maximize_beautiful_substrings/` | Maximize Beautiful Substrings | MathWorks (IITB) Question 3 |
| `-13` | `q13_path_via_node_edges_paid_once/` | Shortest Route Through a Checkpoint, Edges Paid Once | MathWorks Q1 ("min dist to go from a to b via c, if I traverse an edge once its weight is not counted next time") |
| `-14` | `q14_prime_factor_bulbs/` | Prime Factor Bulbs | MathWorks Q2 ("find their prime factors... bulbs[i] = 1 means on... for each prime factor change that bulb's state") |
| `-15` | `q15_mirrored_reversals/` | Mirrored Reversals | MathWorks Q3 ("for each number[i] reverse the string from numbers[i] to s.size()-1-numbers[i]") |
| `-16` | `q16_count_fixed_bound_subarrays/` | Count Subarrays With Fixed Minimum and Maximum | MathWorks OA (recalled problem 1) |
| `-17` | `q17_two_ended_cpu_scheduler/` | Two-Ended CPU Scheduler | MathWorks OA (recalled problem 2) |
| `-18` | `q18_max_weighted_difference_sum/` | Maximum Weighted Difference Sum | Screenshot: getMaxSumOfArray |
| `-19` | `q19_left_then_right_circular_shift/` | Left Then Right Circular Shift | Screenshot (string shifts) |
| `-20` | `q20_closest_pair_of_points/` | Closest Pair of Points | MathWorks CS OA PDF, problem 1 (also IIITH compendium, 4.1) |
| `-21` | `q21_order_layers_by_efficiency/` | Order Layers by Efficiency | MathWorks CS OA PDF, problem 3 ("Minimum Operations to Make Efficiencies Strictly Increasing") |
| `-22` | `q22_smallest_string_with_123_swaps/` | Smallest String with 1-2-3 Swaps | MathWorks IIITH 2026, Engineering group coding question 3.1 (Number Game) |
| `-23` | `q23_perfect_square_product_subarrays/` | Perfect-Square Product Subarrays | MathWorks IIITH 2026, additional problem 4.2 |

## How to run

```
python driver.py --list           # show the questions
python driver.py -1 -s            # sample tests only (like LeetCode's Run)
python driver.py -1               # all tests, stop at the first failure (like Submit)
python driver.py -1 --case 7      # one test, full input / output / expected
python driver.py -1 --all         # don't stop at the first failure
python driver.py -1 --reset       # restore the blank template
```

Edit only `q<k>_<name>/solution.cpp`. Read the statement in `PROBLEM.md` next to it.
The judge harness lives in `_mathworks/` (reads stdin, calls your `Solution`, prints the answer; don't edit it).
Verdicts: Accepted, Wrong Answer, Time Limit Exceeded (2 s per test), Runtime Error, Compile Error.
Output is compared token by token.

## Requirements

- Python 3.8+
- g++ with C++17 (set `CXX` to use another compiler)

## What the tests cover

Tests run from small to large, so a slow solution passes the early tests and then hits the time limit.

| Question | Tests | Edge cases covered | Wrong approaches they catch |
|---|---|---|---|
| Q1 | 25 (2 samples) | n = 1, k = 0 and k = n, all equal, ties in frequency | most-frequent-first, `k > f`, distinct − k |
| Q2 | 25 (2 samples) | one value, all distinct, a count that forces size 1 groups, sizes that need a scan down from min count | only size = min count, floor division, #distinct |
| Q3 | 24 (2 samples) | 1, 10^6, largest prime below 10^6, perfect squares, highly composite numbers | proper divisors, double-counted square root, single total |
| Q4 | 28 (2 samples) | n = 1, negative-only arrays (forced picks), pieces covering the whole array, greedy traps, max values | greedy longest-first, "at most" counts, 32-bit overflow |
| Q5 | 25 (2 samples) | k = n−1, k = 1, all-equal string, alternating string, n = 2·10^5 with k = 10^5 | non-overlapping blocks, missing last pair, window k−1 |
| Q6 | 28 (2 samples) | single letters, identical strings, reversed strings, all-z vs all-a, greedy merge traps | merge-sort greedy, forgetting inner inversions, best of a+b / b+a |
| Q7 | 26 (3 samples) | answer 0, touching meetings (half-open), nested meetings, unsorted input, gap exactly k vs k−1 | gap > k, no running max, no sort, ignoring the gap at 0 |
| Q8 | 27 (3 samples) | single element, long carry chains (2^18 zeros), exponent 10^6, all equal | #distinct, odd counts without carry, dropping the final carry |
| Q9 | 26 (3 samples) | already equal, impossible (-1), cheap "middleman" swaps (2·min), sorted-pairing traps, 10^9 values | no 2·min trick, unit cost, pairing sorted excesses |
| Q10 | 28 (3 samples) | n = 1, strict majority vs exactly half, all distinct, many small groups | 1-or-#distinct, reusing the top value, half = majority |
| Q11 | 23 (3 samples) | single letter, all-same 1000 chars, 26 distinct letters, max size (100 × 1000) | all-even only, real palindromes, 16-bit counter |
| Q12 | 29 (3 samples) | all dots, no dots, dots between equal letters (merge), long dot runs, answer > 2^31 | copy previous letter, join longer neighbour, 32-bit overflow |
| Q13 | 24 (3 samples) | a = b = c, unreachable (-1), shared edges, parallel edges, 10^5-node path (answer > 2^31) | d(a,c)+d(c,b), best two pairwise distances, 32-bit overflow |
| Q14 | 26 (3 samples) | number 1, primes > n, repeated prime factors, 0/1 start states, 10^5 × 10^6 | toggle per prime occurrence, 0-indexed bulbs, dropping the last large prime |
| Q15 | 23 (3 samples) | n = 1, middle-only segments, repeated positions, 10^5 reversals on 2·10^5 chars | 1-indexed segment, deduped positions, no prefix parity |
| Q16 | 25 (2 samples) | minK > maxK, minK = maxK, out-of-range breakers, answer ~5·10^9 | ignoring out-of-range values, 32-bit overflow, max of last positions |
| Q17 | 29 (3 samples) | single process, T exactly enough vs one short, both ends finishing together, T up to 10^15 | ignoring turn order, shortest job first, left to right |
| Q18 | 22 (2 samples) | negative maximum (mod fix), n = 1, all equal, sums near 5·10^18 | both sorted ascending, C++ `%` on a negative, 0-indexed weights, 32-bit products |
| Q19 | 25 (3 samples) | n = 1, shifts larger than n, left = right, shift = n | swapped directions, no modulo, ignoring the right shift |
| Q20 | 23 (3 samples) | duplicate points (0), extreme coordinates (answer 8·10^18), points spread on a line, dense grid | adjacent after x-sort, printing sqrt, 32-bit overflow |
| Q21 | 25 (3 samples) | already ordered (0), reversed order with incr 1 (answer ~5·10^9), large increments | counting misplaced layers, non-strict depths, 32-bit overflow |
| Q22 | 30 (3 samples) | single digits, no moves possible, only 1/2 or 2/3 digits, long blocks | sorting the string, only 21→12, all 2s before the first 3 |
| Q23 | 27 (3 samples) | all ones (~2·10^10), all squares, large primes like 199, n = 2·10^5 | primes ≤ 100 only, 32-bit overflow, single elements only |

## How the tests were verified

- Every problem has a reference solution (Python, big integers) and an independent brute force
  (all subsets / interleavings / partitions / BFS over reachable states / unit-by-unit simulation, etc.).
  They agreed on every statement example and on **2,000 seeded random small inputs per problem**
  (20,000 for Q17, the scheduler, because its rules are the fiddliest).
- Expected outputs come from the reference solution. The generator asserts every constraint on every test.
- 3–4 plausible wrong solutions per problem (listed above) were run against the tests: **every one fails at least one test.**
- A correct C++ solution for every question passes 100% of the tests in this judge (slowest test 167 ms).
- Naive C++ solutions (O(n²), O(n·k), unit-by-unit simulation, plain recursion, Bellman-Ford, ...) get
  **Time Limit Exceeded** on the large tests of 14 problems. The exception is Q19: its original constraints
  (n, shifts ≤ 10^5) are small enough that shifting one step at a time still finishes in about 1.2 s.
- The blank templates compile and get Wrong Answer.

## Assumptions

Several statements were recalled from memory. Where something was missing or ambiguous I picked the most
standard reading and wrote it down here and in each `PROBLEM.md`. Tell me if your OA differed and I'll regenerate that question.

Where a source gave no examples (most recollections), the examples were written for this kit; their outputs were computed by the reference solution and confirmed by the brute force.

**Q3. Sum of Divisors of Every Element**

- The recalled line was only "find sum of factors for all elements". I read *factors* as **all positive divisors** and return **one sum per element** (not one grand total). If your OA meant something else (prime factors, or a single total), tell me and I'll regenerate.
- No constraints were recalled; `n ≤ 10^5`, `nums[i] ≤ 10^6` were chosen so that an O(value) loop per element is too slow.

**Q4. Maximum Sum of Fixed-Length Pieces**

- The recalled statement didn't say whether the counts are exact or "at most". I assumed **exactly** x, y and z pieces (so negative numbers may be forced into the answer).
- No constraints were recalled. I chose small ones (n ≤ 300, counts ≤ 25) so the intended DP over (position, pieces used) fits; plain recursion without memoisation times out.

**Q5. Hamming Distance of Consecutive Windows**

- "Consecutive substrings" was read as **overlapping windows that start one position apart** (the reading used in the IIITH compendium). If you remember non-overlapping blocks `s[0..k-1]`, `s[k..2k-1]`, ..., tell me.
- No constraints were recalled; with n = 2·10^5 the direct O(n·k) comparison times out.

**Q6. Merge Two Strings with Minimum Inversions**

- Inversions inside `a` and inside `b` count too (they're part of `t`). The order of each string is fixed, so those can't be avoided.
- Letters are compared alphabetically; equal letters are not an inversion.
- No constraints were recalled; |a|, |b| ≤ 1000 makes an O(|a|·|b|) DP the target.

**Q7. Earliest Common Free Slot**

- Intervals are **half-open**: a meeting `[1, 3)` ends at 3, so a slot may start exactly at 3, and a slot `[t, t+k)` may end exactly when a meeting starts.
- Everyone's intervals are given as one combined list (who is busy doesn't matter, only when).
- There is no end of day: if no gap fits, the answer is the end of the last meeting.

**Q8. Remove Power-of-Two Groups**

- The array holds the **exponents** (the recalled example "[2,4,3,5,6] ... 2^2+2^4+2^5" uses them that way). This is the same task as Codeforces 587A.
- No constraints were recalled beyond "array length 10^5"; I used n ≤ 3·10^5 and exponents up to 10^6.

**Q9. Make Two Rows Equal with Minimum Swap Cost**

- The recollection is unclear about the cross-row cost. I used the standard version of this task (LeetCode 2561 *Rearranging Fruits*): a cross-row swap costs the smaller of the two swapped heights. If your OA charged a flat 1 per swap, tell me and I'll switch it.
- "Same height in the opposite direction" was read as: column `i` of row 1 equals column `i` of row 2.

**Q10. Minimum Subsequences with a Majority Element**

- A subsequence of length 1 always has a majority element.
- No constraints were given; n ≤ 10^5 was assumed.

**Q11. Scatter Palindrome Substrings**

- The PDF's example text was self-contradictory ("abca qualifies... actually it does not"). The rule used is the standard one: a substring qualifies when **at most one** letter has an odd count.

**Q12. Maximize Beautiful Substrings**

- A run of `L` equal letters contains `L·(L+1)/2` beautiful substrings.
- No constraints were given; |s| ≤ 10^5 was assumed.

**Q13. Shortest Route Through a Checkpoint, Edges Paid Once**

- Input order: `n m` on the first line, then `a b c`, then the edges.

**Q14. Prime Factor Bulbs**

- The recollection was short. Assumptions: bulbs are **1-indexed** by the prime itself, each number toggles each of its **distinct** primes once (12 toggles bulb 2 once, not twice), and primes > n are ignored. Another plausible reading is "toggle every bulb whose index is a multiple of p"; tell me if your OA was that one.

**Q15. Mirrored Reversals**

- Positions are 0-indexed, as in the recollection (`numbers[i]` to `s.size()-1-numbers[i]`). This is Codeforces 525B with 0-based indices.
- No constraints were recalled; with these sizes, reversing each segment directly times out.

**Q16. Count Subarrays With Fixed Minimum and Maximum**

- minK may be greater than maxK; then the answer is 0. Same task as LeetCode 2444.

**Q17. Two-Ended CPU Scheduler**

- The alternation never resets: after a left unit, the next unit always goes right, even if the left process just finished.
- A process that finishes exactly at unit `T` counts.
- No constraints were recalled; with T up to 10^15 a unit-by-unit simulation is too slow.

**Q18. Maximum Weighted Difference Sum**

- The screenshot was cut off before the constraints; the constraints above are assumed.
- The maximum sum can be negative. It's reduced to the range [0, 10^9 + 6] the mathematical way (−3 → 1000000004). Example 2 was added for this case, and its output was computed by the reference solution.

**Q19. Left Then Right Circular Shift**

- Shift amounts may be larger than the string length; a shift by k is the same as a shift by k mod n.

**Q20. Closest Pair of Points**

- Same task as CSES 2194 (Minimum Euclidean Distance). The O(N²) all-pairs check times out.

**Q21. Order Layers by Efficiency**

- The PDF itself says the wording was reconstructed and the exact rule wasn't preserved. I used the standard form of this task (it matches the Codeforces *frog sort* setup: positions, weights and jump lengths): depth = position, efficiency = weight, incr = jump length, and the final order of depths must match the order of efficiencies strictly.
- Efficiencies were assumed to be distinct (a permutation), so "strictly increasing" is always reachable.

**Q22. Smallest String with 1-2-3 Swaps**

- Example 3 was added (computed by brute force over all reachable strings).

**Q23. Perfect-Square Product Subarrays**

- The compendium gave n up to 10^5; I raised it to 2·10^5 so an O(n²) scan reliably times out. Examples were written for this kit (no examples were recalled).

### Recalled questions that were left out

- **"Subset OR excluding present values"** (WhatsApp list, 3rd item; IIITH 4.9): the objective wasn't captured
  (count? maximum? over which subsets?). Even the compendium marks it unresolved.
- **"Priority reduction: maximum distinct elements"** (IIITH 3.2): the compendium says the objective is ambiguous, and
  with only the values 1, 2, 3 the answer is at most 3.
- **"Maximum picks with one skip"** (IIITH 4.3): the skip rule and stopping condition weren't recorded.

If you remember any of these more precisely, send it and I'll add it as Q24+.

## Practice problems

| Question | Exact match | Similar problems |
|---|---|---|
| Q1 Least Number of Unique Integers after K Removals | [LeetCode 1481](https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/) | [LC 1338 Reduce Array Size to The Half](https://leetcode.com/problems/reduce-array-size-to-the-half/); [LC 347 Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) |
| Q2 Minimum Number of Groups to Create a Valid Assignment | [LeetCode 2910](https://leetcode.com/problems/minimum-number-of-groups-to-create-a-valid-assignment/) | [LC 914 X of a Kind in a Deck of Cards](https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/); [LC 2870 Minimum Number of Operations to Make Array Empty](https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/) |
| Q3 Sum of Divisors of Every Element | No exact match | [LC 1390 Four Divisors](https://leetcode.com/problems/four-divisors/) (divisor sums per element); [CSES 1713 Counting Divisors](https://cses.fi/problemset/task/1713) (sieve over all values) |
| Q4 Maximum Sum of Fixed-Length Pieces | No exact match | [LC 689 Maximum Sum of 3 Non-Overlapping Subarrays](https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/); [LC 1031 Maximum Sum of Two Non-Overlapping Subarrays](https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/) |
| Q5 Hamming Distance of Consecutive Windows | No exact match | [LC 461 Hamming Distance](https://leetcode.com/problems/hamming-distance/); [LC 1456 Maximum Number of Vowels in a Substring of Given Length](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/) (sliding window) |
| Q6 Merge Two Strings with Minimum Inversions | No exact match | [CF 1601C Optimal Insertion](https://codeforces.com/problemset/problem/1601/C) (minimise inversions while merging); [LC 97 Interleaving String](https://leetcode.com/problems/interleaving-string/) (DP over a merge) |
| Q7 Earliest Common Free Slot | No exact match | [LC 1229 Meeting Scheduler](https://leetcode.com/problems/meeting-scheduler/) (premium); [LC 759 Employee Free Time](https://leetcode.com/problems/employee-free-time/) (premium); [LC 56 Merge Intervals](https://leetcode.com/problems/merge-intervals/) |
| Q8 Remove Power-of-Two Groups | [Codeforces 587A Duff and Weight Lifting](https://codeforces.com/problemset/problem/587/A) | [CF 1095C Powers Of Two](https://codeforces.com/problemset/problem/1095/C); [LC 2571 Minimum Operations to Reduce an Integer to 0](https://leetcode.com/problems/minimum-operations-to-reduce-an-integer-to-0/) |
| Q9 Make Two Rows Equal with Minimum Swap Cost | [LeetCode 2561 Rearranging Fruits](https://leetcode.com/problems/rearranging-fruits/) (under the assumed cost rule) | [LC 1247 Minimum Swaps to Make Strings Equal](https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/); [LC 1007 Minimum Domino Rotations For Equal Row](https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/) |
| Q10 Minimum Subsequences with a Majority Element | No exact match | [LC 169 Majority Element](https://leetcode.com/problems/majority-element/); [LC 2780 Minimum Index of a Valid Split](https://leetcode.com/problems/minimum-index-of-a-valid-split/) |
| Q11 Scatter Palindrome Substrings | No exact match on LeetCode | [LC 1915 Number of Wonderful Substrings](https://leetcode.com/problems/number-of-wonderful-substrings/) (same idea, letters a–j); [LC 1542 Find Longest Awesome Substring](https://leetcode.com/problems/find-longest-awesome-substring/) |
| Q12 Maximize Beautiful Substrings | No exact match | [LC 1759 Count Number of Homogenous Substrings](https://leetcode.com/problems/count-number-of-homogenous-substrings/); [LC 1576 Replace All ?'s to Avoid Consecutive Repeating Characters](https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/) |
| Q13 Shortest Route Through a Checkpoint, Edges Paid Once | No exact match | [LC 2203 Minimum Weighted Subgraph With the Required Paths](https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths/) (directed cousin, same 3-Dijkstra idea); [LC 743 Network Delay Time](https://leetcode.com/problems/network-delay-time/) |
| Q14 Prime Factor Bulbs | No exact match | [LC 2521 Distinct Prime Factors of Product of Array](https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/); [LC 319 Bulb Switcher](https://leetcode.com/problems/bulb-switcher/) |
| Q15 Mirrored Reversals | [Codeforces 525B Pasha and String](https://codeforces.com/problemset/problem/525/B) (1-indexed there) | [LC 541 Reverse String II](https://leetcode.com/problems/reverse-string-ii/); [LC 2381 Shifting Letters II](https://leetcode.com/problems/shifting-letters-ii/) (difference array) |
| Q16 Count Subarrays With Fixed Minimum and Maximum | [LeetCode 2444 Count Subarrays With Fixed Bounds](https://leetcode.com/problems/count-subarrays-with-fixed-bounds/) | [LC 795 Number of Subarrays with Bounded Maximum](https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/); [LC 2762 Continuous Subarrays](https://leetcode.com/problems/continuous-subarrays/) |
| Q17 Two-Ended CPU Scheduler | No exact match | [LC 2073 Time Needed to Buy Tickets](https://leetcode.com/problems/time-needed-to-buy-tickets/); [LC 1423 Maximum Points You Can Obtain from Cards](https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/) (two ends) |
| Q18 Maximum Weighted Difference Sum | No exact match | [LC 1874 Minimize Product Sum of Two Arrays](https://leetcode.com/problems/minimize-product-sum-of-two-arrays/) (premium; rearrangement inequality); [LC 561 Array Partition](https://leetcode.com/problems/array-partition/) |
| Q19 Left Then Right Circular Shift | [LC 1427 Perform String Shifts](https://leetcode.com/problems/perform-string-shifts/) (premium, near-exact) | [LC 796 Rotate String](https://leetcode.com/problems/rotate-string/) |
| Q20 Closest Pair of Points | [CSES 2194 Minimum Euclidean Distance](https://cses.fi/problemset/task/2194) | [LC 973 K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) (warm-up) |
| Q21 Order Layers by Efficiency | No exact match confirmed | [LC 1827 Minimum Operations to Make the Array Increasing](https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/); [LC 945 Minimum Increment to Make Array Unique](https://leetcode.com/problems/minimum-increment-to-make-array-unique/) |
| Q22 Smallest String with 1-2-3 Swaps | No exact match | [CF 1009B Minimum Ternary String](https://codeforces.com/problemset/problem/1009/B) (very close: 0/1/2 with restricted swaps); [LC 1505 Minimum Possible Integer After at Most K Adjacent Swaps On Digits](https://leetcode.com/problems/minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/) |
| Q23 Perfect-Square Product Subarrays | No exact match | [CF 895C Square Subsets](https://codeforces.com/problemset/problem/895/C); [LC 2572 Count the Number of Square-Free Subsets](https://leetcode.com/problems/count-the-number-of-square-free-subsets/); [LC 1915 Number of Wonderful Substrings](https://leetcode.com/problems/number-of-wonderful-substrings/) (prefix-XOR counting) |
