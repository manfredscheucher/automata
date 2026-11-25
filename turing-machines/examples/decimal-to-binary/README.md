# Turing machine: decimal to binary

`decimal-to-binary.txt` turns a decimal number into a binary number with the most significant bit on the left: `13` becomes `1101`, `100` becomes `1100100` (10 states, 75 rules).

It halves the number again and again from left to right, like long division. The states `halve0` and `halve1` remember the remainder so far. At the right end the remainder is the next bit, and it goes in front of the bits behind the `#`. Tape: `<number> # <bits>`.

## Run

```bash
python3 ../../simulator/minituring.py decimal-to-binary.txt 13
```

## See also

The "Decimal to binary" example on [turingmachinesimulator.com](https://turingmachinesimulator.com/) (by Max von Buelow and kd3x, CC BY-NC-SA 3.0 license) halves from right to left, with an extra digit after the decimal point for the 0.5. It writes each remainder at the right end, so its result has the least significant bit on the left: `13` becomes `1011`. Changing two of its rules gives the most significant bit on the left: `setrest0,1` to `setrest1,0,>` and `setrest1,0` to `setrest0,1,>`. Then each new bit goes in front and the others move one cell to the right.
