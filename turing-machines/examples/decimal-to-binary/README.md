# Turing machine: decimal to binary

Both machines turn a decimal number into a binary number with the most significant bit on the left: `13` becomes `1101`, `100` becomes `1100100`.

| File | How | States | Rules | Steps for 13 / 1000 |
| --- | --- | ---: | ---: | ---: |
| `decimal-to-binary-msb.txt` | the "Decimal to binary" example, 2 rules changed | 14 | 68 | 68 / 246 |
| `decimal-to-binary.txt` | halves from left to right, the remainder is in the state | 10 | 75 | 43 / 181 |

The original "Decimal to binary" example turns a decimal number (most significant digit on the left) into a binary number with the least significant bit on the left: `13` becomes `1011`. It halves the decimal number from right to left, with an extra digit after the decimal point for the 0.5, and writes each remainder at the right end. In `decimal-to-binary-msb.txt` two rules are changed (`setrest0,1` and `setrest1,0`): each new bit goes in front and the others move one cell to the right.

`decimal-to-binary.txt` halves from left to right, like long division. The states `halve0` and `halve1` remember the remainder so far, so no extra digit is needed. At the right end the remainder is the next bit, and it goes in front of the bits behind the `#`. Tape: `<number> # <bits>`.

```bash
python3 ../../simulator/minituring.py decimal-to-binary-msb.txt 13
python3 ../../simulator/minituring.py decimal-to-binary.txt 13
```

## Source and license

`decimal-to-binary-msb.txt` is a modified version of the "Decimal to binary" example on [turingmachinesimulator.com](https://turingmachinesimulator.com/) by Max von Buelow and kd3x (2013), modified 2026 by Manfred Scheucher. Like the original, it is under the [CC BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/) license.
