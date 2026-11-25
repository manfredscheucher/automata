# Turing machines

Turing machines with one tape, in the format of [turingmachinesimulator.com](https://turingmachinesimulator.com/).

- [simulator](simulator): minituring, a minimal Turing machine simulator in Python, and converters between the two formats
- [examples/palindrome](examples/palindrome): a simplified version of the "Binary palindrome" example
- [examples/duplicate](examples/duplicate): the "Duplicate binary string" example, generalized from 0,1 to 0 to 3 and 0 to 9, and a real copy, with and without a separator
- [examples/decimal-to-binary](examples/decimal-to-binary): the "Decimal to binary" example, with the most significant bit on the left
- [examples/increment](examples/increment): adding 1 to a binary number, and a counter that never stops
- [examples/turingmachine-io](examples/turingmachine-io): the examples of turingmachine.io, converted to the turingmachinesimulator.com format, among them `repeat-01`, the first machine in Turing's 1936 paper

Every example is there in two formats: `.txt` for [turingmachinesimulator.com](https://turingmachinesimulator.com/) and `.yaml` for [turingmachine.io](https://turingmachine.io/). Paste one into the editor on either site, or run the `.txt` locally:

```bash
python3 simulator/minituring.py examples/palindrome/binary-palindrome-simplified.txt 11011
```
