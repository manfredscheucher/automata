# Turing machine: duplicate a string

Generalized versions of the "Duplicate binary string" example by Gabriel Alvarez on [turingmachinesimulator.com](https://turingmachinesimulator.com/). The machine appends the mirror image of the input, so `0123` becomes `01233210`.

It marks the rightmost unmarked symbol (0 becomes `o`, 1 becomes `i`, ...), carries it to the right end and writes the marker there, and repeats until all symbols are marked. At the end it turns the markers back into symbols.

The original works with 0 and 1. These versions allow more symbols:

| File | Symbols | States | Rules |
| --- | --- | ---: | ---: |
| original | 0, 1 | 6 | 25 |
| `duplicate-0-3.txt` | 0 to 3 | 8 | 55 |
| `duplicate-0-9.txt` | 0 to 9 | 14 | 253 |

The number of rules grows with the square of the number of symbols: every "carry symbol x to the right" state needs a rule for every symbol and every marker.

## A real copy

`duplicate-binary-string.txt` copies the string right behind itself: `01001` becomes `0100101001` (6 states, 23 rules). It works from left to right. Every symbol that is done becomes `o` (for 0) or `i` (for 1): the original once it is copied, and the new copy at the end. So the tape shows what is already copied. At the end all `o` and `i` turn back into 0 and 1.

`copy-binary-string.txt` makes a real copy with a separator: `01001` becomes `01001#01001` (8 states, 25 rules). It works from left to right: it marks the leftmost unmarked symbol, carries it to the right end, and stops at the `#`.

## Source

The original example is by Gabriel Alvarez, from [turingmachinesimulator.com](https://turingmachinesimulator.com/). Generalized 2026 by Manfred Scheucher. `duplicate-0-9.txt` follows the same layout as `duplicate-0-3.txt`.

## Run

Open [turingmachinesimulator.com](https://turingmachinesimulator.com/), paste one of the files into the editor, compile and run it with an input like `0123`.
