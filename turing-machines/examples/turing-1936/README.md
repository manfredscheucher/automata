# Turing machine: the first machine from 1936

`repeat-01.txt` is the first example machine in Alan Turing's 1936 paper "On Computable Numbers, with an Application to the Entscheidungsproblem". On an empty tape it writes 0 1 0 1 ... forever, with an empty cell after each symbol (4 states, 4 rules).

## Run

```bash
python3 ../../simulator/minituring.py repeat-01.txt ""
```

It never stops; minituring stops it after 10000 steps.

## Source

From the [turingmachine.io](https://turingmachine.io/) examples by Andy Li ([turing-machine-viz](https://github.com/aepsilon/turing-machine-viz/tree/master/src/examples)), converted to the turingmachinesimulator.com format with the comments and exercises kept. Copyright 2015-2021 Andy Li, BSD 3-Clause license, see [LICENSE-turingmachine-io](../LICENSE-turingmachine-io).
