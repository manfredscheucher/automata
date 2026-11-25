# Turing machine: duplicate a string

These machines make a real copy of a binary string. For the mirror image, which makes a palindrome, see [palindrome-build](../palindrome-build).

| File | Result for `01001` | States | Rules |
| --- | --- | ---: | ---: |
| `duplicate.txt` | `0100101001` | 6 | 23 |
| `duplicate-separator.txt` | `01001#01001` | 8 | 25 |

Both work from left to right: take the next symbol, carry it to the right end, write it there, go back.

- `duplicate.txt` turns every symbol that is done into `o` (for 0) or `i` (for 1): the original once it is copied, and the new copy at the end. So the tape shows what is already copied. At the end all `o` and `i` turn back into 0 and 1.
- `duplicate-separator.txt` first writes a `#` at the end, and stops when it reaches the `#`.

## Run

```bash
python3 ../../simulator/minituring.py duplicate.txt 01001
python3 ../../simulator/minituring.py duplicate-separator.txt 01001
```
