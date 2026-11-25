# Turing machine: decimal to binary

`decimal-to-binary-msb.txt` turns a decimal number into a binary number with the most significant bit on the left: `13` becomes `1101`, `100` becomes `1100100`.

It halves the decimal number again and again and keeps the remainders. The original writes each new remainder at the right end, so its result has the least significant bit on the left (`1011` for 13). Here two rules are changed (`setrest0,1` and `setrest1,0`): each new bit goes in front and the others move one cell to the right.

```bash
python3 ../simulator/minituring.py decimal-to-binary-msb.txt 13
```

## Source and license

Modified version of the "Decimal to binary" example on [turingmachinesimulator.com](https://turingmachinesimulator.com/) by Max von Buelow and kd3x (2013), modified 2026 by Manfred Scheucher. Like the original, it is under [CC BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/).
