# Turing machine: binary counter

| File | What it does | States | Rules |
| --- | --- | ---: | ---: |
| `counter.txt` | counts forever: 0, 1, 10, 11, 100, ... (on a blank tape it writes 0 first) | 3 | 9 |
| `increment.txt` | adds 1 once and stops: `1011` becomes `1100` | 4 | 9 |
| `increment-original.txt` | the same, but stops one cell left of the last digit it changed | 3 | 6 |

Both go to the rightmost digit and add 1 there: a 1 becomes 0 and the carry moves one digit to the left, a 0 (or a blank) becomes 1. The increment then goes back to the first digit and stops. The counter goes to the rightmost digit again for the next +1.

## Run

```bash
python3 ../../simulator/minituring.py counter.txt ""
python3 ../../simulator/minituring.py increment.txt 1011
python3 ../../simulator/minituring.py increment-original.txt 1011
```

The counter never stops; minituring stops it after 10000 steps.

## Source

Both are based on the turingmachine.io example [binaryIncrement.yaml](https://github.com/aepsilon/turing-machine-viz/blob/master/src/examples/binaryIncrement.yaml), Copyright 2015-2021 Andy Li, BSD 3-Clause license, see [LICENSE-turingmachine-io](../LICENSE-turingmachine-io). The unchanged port is `increment-original.txt`. Going back to the first digit is the first exercise of that example; the counter loops the increment. Modified 2026 by Manfred Scheucher.
