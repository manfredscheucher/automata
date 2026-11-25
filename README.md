# Automata

Work in progress. Programs and small simulators for machines that compute, from my videos in the playlist [How Computers Work](https://www.youtube.com/playlist?list=PLU1OJ36r4v_c).

So far: Turing machines with one tape, in the format of [turingmachinesimulator.com](https://turingmachinesimulator.com/).

- [simulator](simulator): minituring, a minimal Turing machine simulator in Python
- [palindrome](palindrome): a simplified version of the "Binary palindrome" example
- [duplicate](duplicate): the "Duplicate binary string" example, generalized from 0,1 to 0 to 3 and 0 to 9, and a real copy, with and without a separator
- [decimal-to-binary](decimal-to-binary): the "Decimal to binary" example, with the most significant bit on the left
- [increment](increment): adding 1 to a binary number, and a counter that never stops
- [turingmachine-io](turingmachine-io): the examples of turingmachine.io, converted to the turingmachinesimulator.com format, among them `repeat-01`, the first machine in Turing's 1936 paper

Every example is there in two formats: `.txt` for [turingmachinesimulator.com](https://turingmachinesimulator.com/) and `.yaml` for [turingmachine.io](https://turingmachine.io/). Paste one into the editor on either site, or run the `.txt` locally:

```bash
python3 simulator/minituring.py palindrome/binary-palindrome-simplified.txt 11011
```
