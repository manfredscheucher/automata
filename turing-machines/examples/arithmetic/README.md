# Turing machine: arithmetic

| File | What it does | States | Rules |
| --- | --- | ---: | ---: |
| `binary-add.txt` | adds two binary numbers: `1011+11001` leaves `100100 11001`, the sum and then the second number | 11 | 43 |
| `binary-mult.txt` | multiplies two binary numbers: `11*101` becomes `1111` (3 · 5 = 15) | 21 | 70 |
| `unary-mult.txt` | multiplies two unary numbers: `||*|||` gets `||||||` appended (2 · 3 = 6) | 10 | 19 |

## Run

```bash
python3 ../../simulator/minituring.py binary-add.txt 1011+11001
python3 ../../simulator/minituring.py binary-mult.txt '11*101'
python3 ../../simulator/minituring.py unary-mult.txt '||*|||'
```

## Source

From the [turingmachine.io](https://turingmachine.io/) examples by Andy Li ([turing-machine-viz](https://github.com/aepsilon/turing-machine-viz/tree/master/src/examples)), converted to the turingmachinesimulator.com format with the comments and exercises kept. Copyright 2015-2021 Andy Li, BSD 3-Clause license, see [LICENSE-turingmachine-io](../LICENSE-turingmachine-io).
