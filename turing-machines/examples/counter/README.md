# Turing machine: binary counter

| File | What it does | States | Rules |
| --- | --- | ---: | ---: |
| `binary-increment-back.txt` | adds 1 to a binary number and stops (`1011` -> `1100`) | 4 | 9 |
| `binary-counter.txt` | adds 1 in a loop and never stops; on a blank tape it writes 0 first: 0, 1, 10, 11, ... | 3 | 9 |

Both go to the rightmost digit and add 1 there: a 1 becomes 0 and the carry moves one digit to the left, a 0 (or a blank) becomes 1. The increment then goes back to the first digit and stops, the counter goes to the rightmost digit again for the next +1.

## Run

```bash
python3 ../../simulator/minituring.py binary-increment-back.txt 1011
python3 ../../simulator/minituring.py binary-counter.txt ""
```

The counter runs until minituring stops it after 10000 steps.

## Source

Both are based on the turingmachine.io example `binaryIncrement` by Andy Li ([binaryIncrement.yaml](https://github.com/aepsilon/turing-machine-viz/blob/master/src/examples/binaryIncrement.yaml), Copyright 2015-2021 Andy Li, BSD 3-Clause license, see [LICENSE](../turingmachine-io/LICENSE)); the unchanged port is [../turingmachine-io/binary-increment.txt](../turingmachine-io/binary-increment.txt). Going back to the first digit is the first exercise of that example. The counter loops the increment and writes 0 on a blank tape.
