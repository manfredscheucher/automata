# Turing machine: languages

These machines decide whether the input belongs to a language: they accept or reject it.

| File | Language | Example | States | Rules |
| --- | --- | --- | ---: | ---: |
| `match-binary-strings.txt` | w#w, two equal binary strings | `01001#01001` | 8 | 20 |
| `match-three-lengths.txt` | aⁿbⁿcⁿ | `aabbcc` | 6 | 16 |
| `length-mult.txt` | aⁱbʲcᵏ with i · j = k | `aabbbcccccc` | 12 | 28 |
| `powers-of-two.txt` | 0s whose length is a power of two | `0000` | 7 | 14 |

## Run

```bash
python3 ../../simulator/minituring.py match-binary-strings.txt 01001#01001
python3 ../../simulator/minituring.py match-three-lengths.txt aabbcc
python3 ../../simulator/minituring.py length-mult.txt aabbbcccccc
python3 ../../simulator/minituring.py powers-of-two.txt 0000
```

## Source

From the [turingmachine.io](https://turingmachine.io/) examples by Andy Li ([turing-machine-viz](https://github.com/aepsilon/turing-machine-viz/tree/master/src/examples)), converted to the turingmachinesimulator.com format with the comments and exercises kept. Copyright 2015-2021 Andy Li, BSD 3-Clause license, see [LICENSE-turingmachine-io](../LICENSE-turingmachine-io).
