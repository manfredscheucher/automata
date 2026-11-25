# Turing machine: check for a palindrome

A simplified version of the "Binary palindrome" example on [turingmachinesimulator.com](https://turingmachinesimulator.com/). The original is here unchanged as `palindrome-check-original.txt`.

The original works in two phases. It erases the leftmost symbol, remembers it, walks to the right end and erases the matching symbol there (or rejects). Then it does the same from the right end back to the left. The simplified version drops the second phase and just walks back to the left end.

| | `palindrome-check-original.txt` | `palindrome-check-simplified.txt` |
| --- | ---: | ---: |
| States | 12 | 7 |
| Rules | 30 | 16 |

The trade-off: nearly half the states and rules, but nearly double the number of steps, because the walk back to the left does no work.

## Run

```bash
python3 ../../simulator/minituring.py palindrome-check-original.txt 10101
python3 ../../simulator/minituring.py palindrome-check-simplified.txt 10101
```

## Source

The original example is by Martin Ugarte (Copyleft 2017), from [turingmachinesimulator.com](https://turingmachinesimulator.com/). Modified 2026 by Manfred Scheucher.
