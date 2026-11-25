# Turing machine: binary increment and counter

| File | What it does | States | Rules |
| --- | --- | ---: | ---: |
| `binary-increment.txt` | adds 1 to a binary number and stops (`1011` -> `1100`) | 4 | 9 |
| `binary-counter.txt` | adds 1 in a loop and never stops: 1, 10, 11, 100, ... | 2 | 6 |

Both go to the rightmost digit and add 1 there: a 1 becomes 0 and the carry moves one digit to the left, a 0 (or a blank) becomes 1. The increment then goes back to the first digit and stops, the counter goes to the rightmost digit again for the next +1.

```bash
python3 ../simulator/minituring.py binary-increment.txt 1011
python3 ../simulator/minituring.py binary-counter.txt ""
```

The counter runs until minituring stops it after 100000 steps.
