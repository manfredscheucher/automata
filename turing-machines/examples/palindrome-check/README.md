# Turing machine: check for a palindrome

These machines check whether a binary string is a palindrome, that is, the same read from both sides: `10101` is accepted, `10` is rejected.

| File | States | Rules |
| --- | ---: | ---: |
| `palindrome-check-original.txt` | 12 | 30 |
| `palindrome-check-simplified.txt` | 7 | 16 |

The original works in two phases. It erases the leftmost symbol, remembers it, walks to the right end and erases the matching symbol there (or rejects). Then it does the same from the right end back to the left. The simplified version drops the second phase and just walks back to the left end. The trade-off: nearly half the states and rules, but nearly double the number of steps, because the walk back to the left does no work.

## Run

```bash
python3 ../../simulator/minituring.py palindrome-check-original.txt 10101
python3 ../../simulator/minituring.py palindrome-check-simplified.txt 10101
```

## Source

The original is the "Binary palindrome" example by Martin Ugarte on [turingmachinesimulator.com](https://turingmachinesimulator.com/), here unchanged. The simplified version is modified 2026 by Manfred Scheucher.
