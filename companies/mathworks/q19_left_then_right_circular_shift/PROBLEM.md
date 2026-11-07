# Q19. Left Then Right Circular Shift

Run: `python driver.py -19`  ·  Edit: `solution.cpp` in this folder
Category: Strings  ·  Source: Screenshot (string shifts)

## Problem Description

You are given a string `s` and two integers `leftShifts` and `rightShifts`. Perform the following operations, in order:

1. Perform a circular left shift on `s` by `leftShifts` positions.
2. On the resulting string, perform a circular right shift by `rightShifts` positions.

Return the final string after performing both operations.

A **circular left shift** by k positions moves the first k characters of the string to the end. A **circular right shift** by k positions moves the last k characters of the string to the beginning.

## Function signature

```cpp
// s : the string, leftShifts / rightShifts : shift amounts
// Return s after a circular left shift by leftShifts, then a circular right shift by rightShifts.
string getShiftedString(string s, int leftShifts, int rightShifts);
```

## Input Format

```
s
leftShifts rightShifts
```

## Output Format

The final string.

## Constraints

- 1 ≤ s.length ≤ 10^5
- 1 ≤ leftShifts, rightShifts ≤ 10^5
- `s` consists of lowercase English letters.

## Example 1

Input:
```
abcdef
2 3
```
Output:
```
fabcde
```
Explanation: "abcdef" left-shifted by 2 becomes "cdefab". Right-shifting "cdefab" by 3 gives "fabcde".

## Example 2

Input:
```
hello
3 1
```
Output:
```
llohe
```
Explanation: "hello" left-shifted by 3 becomes "lohel". Right-shifting "lohel" by 1 gives "llohe".

## Example 3

Input:
```
abcdef
5 2
```
Output:
```
defabc
```
Explanation: "abcdef" left-shifted by 5 becomes "fabcde". Right-shifting "fabcde" by 2 gives "defabc".

## Notes / Assumptions

- Shift amounts may be larger than the string length; a shift by k is the same as a shift by k mod n.
