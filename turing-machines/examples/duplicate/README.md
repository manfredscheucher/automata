# Turing machine: duplicate a string

Two kinds of machines: the `duplicate-0-*` files append the mirror image of the input (`0123` becomes `01233210`), the `copy-binary-string-*` files make a real copy (`01001` becomes `0100101001`).

## Mirror image

The `duplicate-0-*` files are based on the "Duplicate binary string" example by Gabriel Alvarez on [turingmachinesimulator.com](https://turingmachinesimulator.com/). It marks the rightmost unmarked symbol (0 becomes `o`, 1 becomes `i`, ...), carries it to the right end and writes the marker there, and repeats until all symbols are marked. At the end it turns the markers back into symbols.

The original works with 0 and 1. `duplicate-0-1.txt` is the original without 4 rules that never run. The other versions allow more symbols:

| File | Symbols | States | Rules |
| --- | --- | ---: | ---: |
| original | 0, 1 | 6 | 25 |
| `duplicate-0-1.txt` | 0, 1 | 6 | 21 |
| `duplicate-0-3.txt` | 0 to 3 | 8 | 55 |
| `duplicate-0-9.txt` | 0 to 9 | 14 | 253 |

The number of rules grows with the square of the number of symbols: every "carry symbol x to the right" state needs a rule for every symbol and every marker.

## A real copy

`copy-binary-string-no-separator.txt` copies the string right behind itself: `01001` becomes `0100101001` (6 states, 23 rules). It works from left to right. Every symbol that is done becomes `o` (for 0) or `i` (for 1): the original once it is copied, and the new copy at the end. So the tape shows what is already copied. At the end all `o` and `i` turn back into 0 and 1.

`copy-binary-string.txt` makes a real copy with a separator: `01001` becomes `01001#01001` (8 states, 25 rules). It works from left to right: it marks the leftmost unmarked symbol, carries it to the right end, and stops at the `#`.

## Run

```bash
python3 ../../simulator/minituring.py duplicate-0-3.txt 0123
python3 ../../simulator/minituring.py copy-binary-string-no-separator.txt 01001
```

## Source

The original example is by Gabriel Alvarez, from [turingmachinesimulator.com](https://turingmachinesimulator.com/). Modified 2026 by Manfred Scheucher: generalized to more symbols, and rules that never run removed. `duplicate-0-9.txt` follows the same layout as `duplicate-0-3.txt`.
