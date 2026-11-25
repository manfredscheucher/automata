# Turing machine: duplicate a string

Two machines that make a real copy of a binary string, both from left to right. For the mirror image, which makes a palindrome (`0123` becomes `01233210`), see [palindrome-build](../palindrome-build).

`duplicate.txt` copies the string right behind itself: `01001` becomes `0100101001` (6 states, 23 rules). Every symbol that is done becomes `o` (for 0) or `i` (for 1): the original once it is copied, and the new copy at the end. So the tape shows what is already copied. At the end all `o` and `i` turn back into 0 and 1.

`duplicate-separator.txt` makes a real copy with a separator: `01001` becomes `01001#01001` (8 states, 25 rules). It marks the leftmost unmarked symbol, carries it to the right end, and stops at the `#`.

## Run

```bash
python3 ../../simulator/minituring.py duplicate.txt 01001
python3 ../../simulator/minituring.py duplicate-separator.txt 01001
```
