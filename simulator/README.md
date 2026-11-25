# minituring: a minimal Turing machine simulator

A Turing machine simulator in Python, kept short and easy to follow. Like [minisim](https://github.com/manfredscheucher/ktoy#minisim) for the Toy CPU.

It reads programs in the format of [turingmachinesimulator.com](https://turingmachinesimulator.com/) (one tape): `//` comments, `init:` and `accept:`, and each rule on two lines:

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
python3 minituring.py ../palindrome/binary-palindrome-simplified.txt 11011
```

It prints every step with the state and the tape (head in `[ ]`), and stops after 100000 steps if the machine doesn't halt.

## Several tapes

`multituring.py` is the same for machines with several tapes, in the multi-tape format of turingmachinesimulator.com. A rule for 2 tapes reads one symbol per tape and writes and moves on each tape:

```
copy,1,_
copy,1,1,>,>
```

The input goes on tape 1, the other tapes start blank. The tapes are one dictionary from (tape, position) to symbol.

```bash
python3 multituring.py ../multitape/palindrome-2-tapes.txt 11011
```
