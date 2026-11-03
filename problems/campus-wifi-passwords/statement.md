You are given an alphanumeric string `str` (containing only English letters `a-z`, `A-Z`, and digits `0-9`), representing an initial university campus Wi-Fi password.

To generate valid alternate passwords, you must rearrange all characters of `str` such that:

1. All **digits** (`0-9`) appear in the initial (**prefix**) positions of the string.
2. All **alphabetic characters** (`a-z`, `A-Z`) appear in the remaining (**suffix**) positions of the string.

Generate and print all **distinct** valid rearrangements of `str` in **lexicographically ascending (ASCII) order**.

### Input
A single line containing an alphanumeric string `str` without spaces.

### Output
Print all distinct valid password permutations in lexicographical (ASCII) ascending order, separated by spaces (or newlines).

### Constraints
- $1 \le |str| \le 8$
- `str` consists only of digits (`0-9`), uppercase letters (`A-Z`), and lowercase letters (`a-z`).

### Explanation of Example 1
- Digits in `aB3`: `{'3'}`
- Letters in `aB3`: `{'B', 'a'}`
- Placing digits first and letters last gives two valid permutations: `"3Ba"` and `"3aB"` (since uppercase `'B'` has ASCII `66` and lowercase `'a'` has ASCII `97`, `"3Ba"` comes first).

### Explanation of Example 2
- Digits: `{'1', '2'}` $\to$ permutations in ascending order: `"12"`, `"21"`
- Letters: `{'a', 'b'}` $\to$ permutations in ascending order: `"ab"`, `"ba"`
- Combining every digit permutation with every letter permutation in lexicographical order yields: `12ab 12ba 21ab 21ba`.

### Explanation of Example 3
- Duplicate characters produce only **distinct** permutations: digits `{'1', '1'}` give `"11"`, and letters `{'A', 'a'}` give `"Aa"`, `"aA"`, yielding `11Aa 11aA`.

