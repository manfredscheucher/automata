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

## Examples

Run from this folder. The result column shows what is on the tape at the end.

| What | Command | Result |
| --- | --- | --- |
| binary palindrome | `python3 minituring.py ../palindrome/binary-palindrome-simplified.txt 11011` | accepted after 21 steps, tape empty (the machine erases the input) |
| copy with separator | `python3 minituring.py ../duplicate/copy-binary-string.txt 01001` | accepted after 84 steps, tape `01001#01001` |
| append the mirror image | `python3 minituring.py ../duplicate/duplicate-0-3.txt 0123` | accepted after 51 steps, tape `01233210` |
| add 1 | `python3 minituring.py ../turingmachine-io/binary-increment.txt 1011` | accepted after 8 steps, tape `1100` |
| add two binary numbers | `python3 minituring.py ../turingmachine-io/binary-add.txt 1011+11001` | accepted after 92 steps, tape `100100_11001` (the sum, then the second number) |
| multiply two binary numbers | `python3 minituring.py ../turingmachine-io/binary-mult.txt '11*101'` | accepted after 116 steps, tape `1111` |
| divisible by 3 | `python3 minituring.py ../turingmachine-io/divisible-by-3.txt 1001` | accepted after 5 steps, tape `1001` |
| busy beaver with 3 states | `python3 minituring.py ../turingmachine-io/busy-beaver-3.txt ""` | accepted after 13 steps, tape `111111` |
