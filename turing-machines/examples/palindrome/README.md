# Turing machine: binary palindrome

A simplified version of the "Binary palindrome" example on [turingmachinesimulator.com](https://turingmachinesimulator.com/).

The original works in two phases. It erases the leftmost symbol, remembers it, walks to the right end and erases the matching symbol there (or rejects). Then it does the same from the right end back to the left. The simplified version drops the second phase and just walks back to the left end.

| | Original | Simplified |
| --- | ---: | ---: |
| States | 12 | 7 |
| Rules | 30 | 16 |

The trade-off: nearly half the states and rules, but nearly double the number of steps, because the walk back to the left does no work.

## Run

```bash
python3 ../../simulator/minituring.py binary-palindrome-simplified.txt 10101
```

## Source

The original example is by Martin Ugarte (Copyleft 2017), from [turingmachinesimulator.com](https://turingmachinesimulator.com/). Modified 2026 by Manfred Scheucher.
