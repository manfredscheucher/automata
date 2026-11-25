# Simulator and converters

`minituring.py` is a Turing machine simulator in Python, kept short and easy to follow, like [minisim](https://github.com/manfredscheucher/ktoy#minisim) for the Toy CPU. `txt2yaml.py` and `yaml2txt.py` convert between the two formats.

minituring reads programs in the format of [turingmachinesimulator.com](https://turingmachinesimulator.com/) (one tape): `//` comments, `init:` and `accept:`, and each rule on two lines:

```
q0,1
qRight1,_,>
```

The first line is the current state and the symbol under the head, the second the next state, the symbol to write and the move (`<`, `>` or `-`). `_` is blank. If no rule matches, the input is rejected.

## Run

```bash
python3 minituring.py <program> <input>
```

For example:

```bash
python3 minituring.py ../examples/palindrome-check/palindrome-check-simplified.txt 11011
```

It prints every step with the state and the tape (head in `[ ]`), and stops after 10000 steps if the machine doesn't halt.

## Convert between the two formats

`txt2yaml.py` converts a program to the YAML format of [turingmachine.io](https://turingmachine.io/), which also draws the states as a diagram. `yaml2txt.py` converts back:

```bash
python3 txt2yaml.py <program.txt> [<input>] > <program>.yaml
python3 yaml2txt.py <program.yaml> > <program>.txt
```

For example:

```bash
python3 txt2yaml.py ../examples/palindrome-check/palindrome-check-simplified.txt 11011
python3 yaml2txt.py ../examples/palindrome-check/palindrome-check-simplified.yaml
```

turingmachine.io has no accepting states (a machine stops when no rule matches), so they are listed in a comment. It can only move left or right, so a rule that stays (`-`) moves right into a helper state that moves back left. `yaml2txt.py` reads the accepting states back from that comment; without it, all states without rules accept, except one called `reject`.

## Examples

Run from this folder. The result column shows what is on the tape at the end.

| What | Command | Result |
| --- | --- | --- |
| check for a palindrome | `python3 minituring.py ../examples/palindrome-check/palindrome-check-simplified.txt 11011` | accepted after 21 steps, tape empty (the machine erases the input) |
| build a palindrome | `python3 minituring.py ../examples/palindrome-build/palindrome-build-0-3.txt 0123` | accepted after 51 steps, tape `01233210` |
| duplicate | `python3 minituring.py ../examples/duplicate/duplicate.txt 01001` | accepted after 102 steps, tape `0100101001` |
| duplicate with separator | `python3 minituring.py ../examples/duplicate/duplicate-separator.txt 01001` | accepted after 84 steps, tape `01001#01001` |
| add 1 | `python3 minituring.py ../examples/counter/increment.txt 1011` | accepted after 10 steps, tape `1100` |
| decimal to binary | `python3 minituring.py ../examples/decimal-to-binary/decimal-to-binary.txt 13` | accepted after 43 steps, tape `1101` |
| add two binary numbers | `python3 minituring.py ../examples/arithmetic/binary-add.txt 1011+11001` | accepted after 92 steps, tape `100100_11001` (the sum, then the second number) |
| multiply two binary numbers | `python3 minituring.py ../examples/arithmetic/binary-mult.txt '11*101'` | accepted after 116 steps, tape `1111` |
| divisible by 3 | `python3 minituring.py ../examples/divisible-by-3/divisible-by-3.txt 1001` | accepted after 5 steps, tape `1001` |
| busy beaver with 3 states | `python3 minituring.py ../examples/busy-beaver/busy-beaver-3.txt ""` | accepted after 13 steps, tape `111111` |
| the first machine in Turing's 1936 paper: 0 1 0 1 ... forever | `python3 minituring.py ../examples/turing-1936/repeat-01.txt ""` | never stops, tape `0_1_0_1_...`; minituring stops it after 10000 steps |
