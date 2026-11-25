# Turing machine: divisible by 3

| File | What it does | States | Rules |
| --- | --- | ---: | ---: |
| `divisible-by-3.txt` | accepts a binary number if it is divisible by 3: `1001` (9) | 4 | 7 |
| `divisible-by-3-base-10.txt` | the same for a decimal number: `4728` | 4 | 31 |

Both read the number once from left to right; the state is the remainder modulo 3 so far.

## Run

```bash
python3 ../../simulator/minituring.py divisible-by-3.txt 1001
python3 ../../simulator/minituring.py divisible-by-3-base-10.txt 4728
```

## Source

From the [turingmachine.io](https://turingmachine.io/) examples by Andy Li ([turing-machine-viz](https://github.com/aepsilon/turing-machine-viz/tree/master/src/examples)), converted to the turingmachinesimulator.com format with the comments and exercises kept. Copyright 2015-2021 Andy Li, BSD 3-Clause license, see [LICENSE-turingmachine-io](../LICENSE-turingmachine-io).
