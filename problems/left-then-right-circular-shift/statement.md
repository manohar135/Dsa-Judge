You are given a string `s` and two integers `leftShifts` and `rightShifts`. Perform the following operations, in order:

1. Perform a circular left shift on `s` by `leftShifts` positions.
2. On the resulting string, perform a circular right shift by `rightShifts` positions.

Return the final string after performing both operations.

A **circular left shift** by k positions moves the first k characters of the string to the end. A **circular right shift** by k positions moves the last k characters of the string to the beginning.

### Input
```
s
leftShifts rightShifts
```

### Output
The final string.

### Constraints
- 1 ≤ s.length ≤ 10^5
- 1 ≤ leftShifts, rightShifts ≤ 10^5
- `s` consists of lowercase English letters.

### Explanation of Example 1
"abcdef" left-shifted by 2 becomes "cdefab". Right-shifting "cdefab" by 3 gives "fabcde".

### Explanation of Example 2
"hello" left-shifted by 3 becomes "lohel". Right-shifting "lohel" by 1 gives "llohe".

### Explanation of Example 3
"abcdef" left-shifted by 5 becomes "fabcde". Right-shifting "fabcde" by 2 gives "defabc".
