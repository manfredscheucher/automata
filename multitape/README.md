# Machines with several tapes

Run them with [multituring](../simulator) or on [turingmachinesimulator.com](https://turingmachinesimulator.com/).

| File | Tapes | States | Rules |
| --- | ---: | ---: | ---: |
| `palindrome-2-tapes.txt` | 2 | 4 | 15 |

`palindrome-2-tapes.txt` copies the input to tape 2 and then compares tape 1 from the left with tape 2 from the right. It needs about 3n steps, the one-tape version in [palindrome](../palindrome) about n²/2.

```bash
python3 ../simulator/multituring.py palindrome-2-tapes.txt 11011
```
