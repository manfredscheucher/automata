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
| [arithmetic](examples/arithmetic) | add and multiply binary numbers, multiply unary numbers |
| [divisible-by-3](examples/divisible-by-3) | check whether a binary or decimal number is divisible by 3 |
| [languages](examples/languages) | decide languages such as w#w and aⁿbⁿcⁿ |
| [busy-beaver](examples/busy-beaver) | the busy beavers with 3 and 4 states |
| [turing-1936](examples/turing-1936) | the first machine in Turing's 1936 paper: 0 1 0 1 ... forever |

Many examples come from [turingmachinesimulator.com](https://turingmachinesimulator.com/) and [turingmachine.io](https://turingmachine.io/); each folder says where its files come from, and [THIRD_PARTY.md](../THIRD_PARTY.md) lists them all.

## Simulator

[simulator](simulator) has minituring, a minimal Turing machine simulator in Python, and two scripts that convert between `.txt` and `.yaml`.

```bash
python3 simulator/minituring.py examples/palindrome-check/palindrome-check-simplified.txt 11011
```
