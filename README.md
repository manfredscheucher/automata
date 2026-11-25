# Automata

Work in progress. Programs and small simulators for machines that compute, from my videos in the playlist [How Computers Work](https://www.youtube.com/playlist?list=PLU1OJ36r4v_c).

So far: Turing machines with one tape and with several tapes, in the format of [turingmachinesimulator.com](https://turingmachinesimulator.com/).

- [simulator](simulator): minituring, a minimal Turing machine simulator in Python, and multituring for several tapes
- [palindrome](palindrome): a simplified version of the "Binary palindrome" example
- [duplicate](duplicate): the "Duplicate binary string" example, generalized from 0,1 to 0 to 3 and 0 to 9, and a real copy with a separator
- [multitape](multitape): machines with several tapes
- [turingmachine-io](turingmachine-io): the examples of turingmachine.io, converted to the turingmachinesimulator.com format

Paste a program into the editor on turingmachinesimulator.com, or run it locally:

```bash
python3 simulator/minituring.py palindrome/binary-palindrome-simplified.txt 11011
python3 simulator/multituring.py multitape/palindrome-2-tapes.txt 11011
```
