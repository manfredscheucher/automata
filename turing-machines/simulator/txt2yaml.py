"""txt2yaml: converts a program from the turingmachinesimulator.com format
to the YAML format of turingmachine.io, so it can be viewed there as well.

Usage:   python3 txt2yaml.py <program> [<input>]  > <program>.yaml
Example: python3 txt2yaml.py ../palindrome/binary-palindrome-simplified.txt 11011

Differences between the two formats:
- The blank _ becomes ' '.
- turingmachine.io has no accepting states: a machine simply stops when no rule
  matches. The accepting states are listed in a comment and appear as states
  without rules.
- turingmachine.io can only move left or right. A rule that stays (-) moves
  right into a helper state, which moves back left.
"""
import sys

BLANK = "_"
MOVES = {"<": "L", ">": "R"}


def symbol(s):
    """A symbol as a quoted YAML string, the blank as ' '."""
    return "' '" if s == BLANK else "'" + s + "'"


def read_program(text):
    """Returns (header comments, name, start state, accepting states, rules).

    Each rule is (state, read, next state, write, move, comments above it).
    """
    header, rules, pending = [], [], []
    name, init, accepting = "", "", []
    lines = [line.strip() for line in text.splitlines()]
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("//"):
            pending.append(line[2:].rstrip())
        elif not line:
            if pending and pending[-1] != "":
                pending.append("")
        elif ":" in line:
            key, value = [x.strip() for x in line.split("//")[0].split(":", 1)]
            if key == "name":
                name = value
            elif key == "init":
                init = value
            elif key == "accept":
                accepting = [s.strip() for s in value.split(",") if s.strip() != "none"]
            if not rules:
                header += pending
                pending = []
        else:
            # A rule: this line and the next line that is not empty or a comment.
            condition = line.split("//")[0]
            i += 1
            while not lines[i] or lines[i].startswith("//"):
                i += 1
            action = lines[i].split("//")[0]
            state, read = [x.strip() for x in condition.split(",")]
            next_state, write, move = [x.strip() for x in action.split(",")]
            while pending and pending[-1] == "":
                pending.pop()
            rules.append((state, read, next_state, write, move, pending))
            pending = []
        i += 1
    return header, name, init, accepting, rules


def convert(text, word=""):
    header, name, init, accepting, rules = read_program(text)
    states = []                       # in order of first appearance
    for state, _, next_state, _, _, _ in rules:
        for s in (state, next_state):
            if s not in states:
                states.append(s)
    with_rules = {state for state, *_ in rules}
    alphabet = sorted({r[1] for r in rules} | {r[3] for r in rules})

    # Rules that stay (-) on a state with rules need a helper state that moves back.
    helpers = {}
    for state, read, next_state, write, move, _ in rules:
        if move == "-" and next_state in with_rules:
            helpers[next_state] = next_state + "Back"

    out = []
    for line in header:
        out.append(("# " + line.strip()) if line.strip() else "")
    while out and out[-1] == "":
        out.pop()
    out.append("")
    if name:
        out.append(f"# {name}")
    out.append("# Converted from the turingmachinesimulator.com format with txt2yaml.py.")
    if accepting:
        out.append(f"# Accepting states: {', '.join(accepting)}. All other stops reject.")
    else:
        out.append("# This machine never stops.")
    out += [f"input: '{word}'", "blank: ' '", f"start state: {init}", "table:"]

    for state in states:
        out.append(f"  {state}:")
        for s, read, next_state, write, move, comments in rules:
            if s != state:
                continue
            for c in comments:
                out.append(f"    # {c.strip()}" if c.strip() else "")
            if move == "-" and next_state in helpers:
                direction, target = "R", helpers[next_state]
            else:
                direction, target = MOVES.get(move, "R"), next_state
            parts = []
            if write != read:
                parts.append(f"write: {symbol(write)}")
            parts.append(direction if target == state else f"{direction}: {target}")
            action = parts[0] if len(parts) == 1 and target == state else "{" + ", ".join(parts) + "}"
            out.append(f"    {symbol(read)}: {action}")
    for target, helper in helpers.items():
        out.append(f"  {helper}:")
        out.append("    # helper: move back left, for a rule that stays in place")
        out.append(f"    [{', '.join(symbol(s) for s in alphabet)}]: {{L: {target}}}")
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    if len(sys.argv) not in (2, 3):
        sys.exit("usage: python3 txt2yaml.py <program> [<input>]")
    word = sys.argv[2] if len(sys.argv) == 3 else ""
    print(convert(open(sys.argv[1]).read(), word), end="")
