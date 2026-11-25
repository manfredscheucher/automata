"""minituring: a minimal Turing machine simulator.

Reads a program in the format of turingmachinesimulator.com (one tape)
and runs it on one input, printing every step.

Usage:   python3 minituring.py <program> <input>
Example: python3 minituring.py palindrome-check-simplified.txt 11011
"""
import sys

BLANK = "_"
MAX_STEPS = 10_000                   # stop machines that never halt
MOVES = {"<": -1, ">": +1, "-": 0}   # head moves left, right or stays


def fields(line, count):
    """Splits "a,b,c" into count stripped parts, or exits with an error."""
    parts = [x.strip() for x in line.split(",")]
    if len(parts) != count:
        sys.exit(f"expected {count} comma-separated values: {line}")
    return parts


def load(text):
    """Parses a program into (start state, accepting states, rules).

    The rules map (state, symbol read) to (next state, symbol to write, move).
    """
    # Drop comments and blank lines.
    lines = []
    for line in text.splitlines():
        line = line.split("//")[0].strip()
        if line:
            lines.append(line)

    # Header lines such as "name: ...", "init: q0" and "accept: qAccept".
    header = {}
    for line in lines:
        if ":" in line:
            key, value = line.split(":", 1)
            header[key.strip()] = value.strip()

    # Every rule takes two lines:
    #   <state>,<read>
    #   <next state>,<write>,<move>
    body = [line for line in lines if ":" not in line]
    if len(body) % 2 != 0:
        sys.exit("every rule needs two lines: <state>,<read> and <next state>,<write>,<move>")

    rules = {}
    for condition, action in zip(body[0::2], body[1::2]):
        state, read = fields(condition, 2)
        next_state, write, move = fields(action, 3)
        if move not in MOVES:
            sys.exit(f"move must be <, > or -: {action}")
        if (state, read) in rules:
            sys.exit(f"two rules for state {state} and symbol {read}")
        rules[(state, read)] = (next_state, write, MOVES[move])

    if "init" not in header or "accept" not in header:
        sys.exit("the program needs an init: and an accept: line")
    accepting = {state.strip() for state in header["accept"].split(",")}
    return header["init"], accepting, rules


def show(tape, head):
    """The written part of the tape, with the head in [ ]."""
    # Show every non-blank cell, and the head even if it stands on a blank.
    cells = [i for i, symbol in tape.items() if symbol != BLANK] + [head]
    text = ""
    for i in range(min(cells), max(cells) + 1):
        symbol = tape.get(i, BLANK)
        text += f"[{symbol}]" if i == head else symbol
    return text


def run(machine, word):
    """Runs the machine on the input word. Returns True if it accepts."""
    state, accepting, rules = machine
    tape = dict(enumerate(word))   # position -> symbol, everything else is blank
    head = 0
    steps = 0

    while True:
        print(f"step={steps} state={state} {show(tape, head)}")

        # Accept in an accepting state, reject if no rule matches.
        rule = rules.get((state, tape.get(head, BLANK)))
        if state in accepting:
            result = "accepted"
        elif rule is None:
            result = "rejected"
        elif steps == MAX_STEPS:
            result = "stopped"
        else:
            result = None
        if result:
            print(f"{result} after {steps} step{'' if steps == 1 else 's'}")
            return result == "accepted"

        # Apply the rule: write, move, change state.
        next_state, write, move = rule
        tape[head] = write
        head += move
        state = next_state
        steps += 1


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit('usage: python3 minituring.py <program> <input>   (use "" for an empty input)')
    program, word = sys.argv[1], sys.argv[2]
    run(load(open(program).read()), word)
