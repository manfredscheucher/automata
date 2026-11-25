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

## Source

The original example is by Gabriel Alvarez, from [turingmachinesimulator.com](https://turingmachinesimulator.com/). Generalized 2026 by Manfred Scheucher. `duplicate-0-9.txt` follows the same layout as `duplicate-0-3.txt`.

## Run

Open [turingmachinesimulator.com](https://turingmachinesimulator.com/), paste one of the files into the editor, compile and run it with an input like `0123`.
