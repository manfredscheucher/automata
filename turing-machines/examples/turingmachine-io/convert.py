"""Converts the turingmachine.io examples (YAML, from turing-machine-viz) to the
turingmachinesimulator.com format, with yaml2txt.py.

Usage: python3 convert.py <turing-machine-viz>/src/examples <output folder>
"""
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "simulator"))
import yaml2txt  # noqa: E402

if __name__ == "__main__":
    src, dst = sys.argv[1], sys.argv[2]
    for f in sorted(os.listdir(src)):
        if not f.endswith(".yaml") or f.startswith("_"):
            continue
        name, settings, states, table, header, notes, footer = yaml2txt.parse(open(os.path.join(src, f)).read())
        intro = [f"// Ported from the turingmachine.io example {f[:-5]}",
                 "// by Andy Li, https://github.com/aepsilon/turing-machine-viz (BSD 3-Clause, see LICENSE)."]
        # binaryIncrement -> binary-increment.txt, divisibleBy3Base10 -> divisible-by-3-base-10.txt
        out = re.sub(r"(?<=[a-z])(?=[A-Z0-9])|(?<=[0-9])(?=[A-Z])", "-", f[:-5]).lower() + ".txt"
        program = yaml2txt.write_program(name, settings, states, table, header, notes, footer, intro)
        open(os.path.join(dst, out), "w").write(program)
        print(out, len(states), "states", sum(len(r) for r in table.values()), "rules")
