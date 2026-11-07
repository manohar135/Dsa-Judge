# Q9. Make Two Rows Equal with Minimum Swap Cost

Run: `python driver.py -9`  ·  Edit: `solution.cpp` in this folder
Category: Greedy / Hash map / Sorting  ·  Source: WhatsApp list: "two rows... make each number in opposite direction have the same height... swap in same row no cost, between rows has cost... min, else -1" (also IIITH compendium, 4.8)

## Problem Description

You have two rows of `n` blocks each; `row1[i]` and `row2[i]` are block heights. You want every column to match: after rearranging, `row1[i] == row2[i]` for every `i`.

- Reordering blocks **inside one row** is free (you may permute each row any way you like).
- **Swapping** a block of `row1` with a block of `row2` costs `min(height1, height2)` of the two swapped blocks.

Return the minimum total cost to make the rows match, or `-1` if it's impossible.

## Function signature

```cpp
// row1, row2 : the two rows (same length)
// Return the minimum total cost to make the rows equal after sorting, or -1.
long long minCost(vector<int>& row1, vector<int>& row2);
```

## Input Format

```
n
row1[0] ... row1[n-1]
row2[0] ... row2[n-1]
```

## Output Format

A single integer: the minimum cost, or -1.

## Constraints

- 1 ≤ n ≤ 10^5
- 1 ≤ row1[i], row2[i] ≤ 10^9
- The answer can exceed 2^31 − 1: use 64-bit integers.

## Example 1

Input:
```
4
4 2 2 2
1 4 1 2
```
Output:
```
1
```
Explanation: Swap a 2 from row 1 with a 1 from row 2 (cost 1). Both rows become {1, 2, 2, 4}.

## Example 2

Input:
```
4
2 3 4 1
3 2 5 1
```
Output:
```
-1
```
Explanation: 4 and 5 each appear once in total, so they can never be matched.

## Example 3

Input:
```
4
5 5 1 1
5 5 1 1
```
Output:
```
0
```
Explanation: Already equal.

## Notes / Assumptions

- The recollection is unclear about the cross-row cost. I used the standard version of this task (LeetCode 2561 *Rearranging Fruits*): a cross-row swap costs the smaller of the two swapped heights. If your OA charged a flat 1 per swap, tell me and I'll switch it.
- "Same height in the opposite direction" was read as: column `i` of row 1 equals column `i` of row 2.
