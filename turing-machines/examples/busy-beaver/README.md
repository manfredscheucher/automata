# Turing machine: busy beaver

A busy beaver is a machine with n states and the symbols 0 and 1 that, started on an empty tape, halts with as many 1s on the tape as possible.

| File | States | Steps | 1s at the end |
| --- | ---: | ---: | ---: |
| `busy-beaver-3.txt` | 3 | 13 | 6 |
| `busy-beaver-4.txt` | 4 | 107 | 13 |

Here 0 is the blank `_`. The state count does not include the halting state.

## Run

```bash
python3 ../../simulator/minituring.py busy-beaver-3.txt ""
python3 ../../simulator/minituring.py busy-beaver-4.txt ""
```

## Source

From the [turingmachine.io](https://turingmachine.io/) examples by Andy Li ([turing-machine-viz](https://github.com/aepsilon/turing-machine-viz/tree/master/src/examples)), converted to the turingmachinesimulator.com format with the comments and exercises kept. Copyright 2015-2021 Andy Li, BSD 3-Clause license, see [LICENSE-turingmachine-io](../LICENSE-turingmachine-io).
