# Turing machine: build a palindrome

These machines append the mirror image of the input: `0123` becomes `01233210`. The result is always a palindrome. The original example is called "Duplicate binary string", but it does not make a real copy; for a real copy (`01001` becomes `0100101001`) see [duplicate](../duplicate).

They are based on the "Duplicate binary string" example by Gabriel Alvarez on [turingmachinesimulator.com](https://turingmachinesimulator.com/). The machine marks the rightmost unmarked symbol (0 becomes `o`, 1 becomes `i`, ...), carries it to the right end and writes the marker there, and repeats until all symbols are marked. At the end it turns the markers back into symbols.

The original, `palindrome-build-original.txt`, works with 0 and 1. `palindrome-build-0-1.txt` is the original without 4 rules that never run. The other versions allow more symbols:

| File | Symbols | States | Rules |
| --- | --- | ---: | ---: |
| `palindrome-build-original.txt` (unchanged) | 0, 1 | 6 | 25 |
| `palindrome-build-0-1.txt` | 0, 1 | 6 | 21 |
| `palindrome-build-0-3.txt` | 0 to 3 | 8 | 55 |
| `palindrome-build-0-9.txt` | 0 to 9 | 14 | 253 |

The number of rules grows with the square of the number of symbols: every "carry symbol x to the right" state needs a rule for every symbol and every marker.

## Run

```bash
python3 ../../simulator/minituring.py palindrome-build-original.txt 01001
python3 ../../simulator/minituring.py palindrome-build-0-3.txt 0123
```

## Source

The original example is by Gabriel Alvarez, from [turingmachinesimulator.com](https://turingmachinesimulator.com/). Modified 2026 by Manfred Scheucher: generalized to more symbols, and rules that never run removed. `palindrome-build-0-9.txt` follows the same layout as `palindrome-build-0-3.txt`.
