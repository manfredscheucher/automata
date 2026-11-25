# Turing machines

Turing machines with one tape. Every example is there twice: as `.txt` for [turingmachinesimulator.com](https://turingmachinesimulator.com/) and as `.yaml` for [turingmachine.io](https://turingmachine.io/). Paste one into the editor on the site, or run the `.txt` with the simulator in this repo.

## Examples

| Folder | What the machines do |
| --- | --- |
| [palindrome-check](examples/palindrome-check) | check whether a binary string is a palindrome |
| [palindrome-build](examples/palindrome-build) | build a palindrome by appending the mirror image: `0123` becomes `01233210` |
| [duplicate](examples/duplicate) | duplicate a binary string: `01001` becomes `0100101001` or `01001#01001` |
| [counter](examples/counter) | count in binary forever, or add 1 once |
| [decimal-to-binary](examples/decimal-to-binary) | turn a decimal number into binary: `13` becomes `1101` |
| [turingmachine-io](examples/turingmachine-io) | the 15 examples of turingmachine.io by Andy Li, among them binary addition and multiplication, two busy beavers, and the first machine in Turing's 1936 paper |

## Simulator

[simulator](simulator) has minituring, a minimal Turing machine simulator in Python, and two scripts that convert between `.txt` and `.yaml`.

```bash
python3 simulator/minituring.py examples/palindrome-check/palindrome-check-simplified.txt 11011
```
