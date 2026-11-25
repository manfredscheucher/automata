# Turing machines

Turing machines with one tape, for [turingmachinesimulator.com](https://turingmachinesimulator.com/) (`.txt`) and [turingmachine.io](https://turingmachine.io/) (`.yaml`).

- [simulator](simulator): minituring, a minimal Turing machine simulator in Python, and converters between the two formats
- [examples/palindrome](examples/palindrome): a simplified version of the "Binary palindrome" example
- [examples/duplicate](examples/duplicate): appending the mirror image (the "Duplicate binary string" example, also for 0 to 3 and 0 to 9), and a real copy, with and without a separator
- [examples/decimal-to-binary](examples/decimal-to-binary): decimal to binary, with the most significant bit on the left
- [examples/increment](examples/increment): adding 1 to a binary number, and a counter that never stops
- [examples/turingmachine-io](examples/turingmachine-io): the examples of turingmachine.io by Andy Li, among them `repeat-01`, the first machine in Turing's 1936 paper

Every example is there as `.txt` and `.yaml`. Paste the `.txt` into the editor on turingmachinesimulator.com or the `.yaml` on turingmachine.io, or run the `.txt` locally:

```bash
python3 simulator/minituring.py examples/palindrome/binary-palindrome-simplified.txt 11011
```
