"""multituring: a minimal Turing machine simulator with several tapes.

Reads a program in the format of turingmachinesimulator.com and runs it on one
input, printing every step. The input goes on tape 1, all other tapes start blank.
For one tape, use minituring.py, which is a bit simpler.

A rule for k tapes takes two lines:
    <state>,<read on tape 1>,...,<read on tape k>
    <next state>,<write on tape 1>,...,<write on tape k>,<move 1>,...,<move k>

Usage:   python3 multituring.py <program> <input>
Example: python3 multituring.py ../multitape/palindrome-2-tapes.txt 11011
"""
import sys

BLANK = "_"
MAX_STEPS = 100_000                  # stop machines that never halt
MOVES = {"<": -1, ">": +1, "-": 0}   # head moves left, right or stays


def load(text):
    """Parses a program into (number of tapes, start state, accepting states, rules).

    The rules map (state, symbols read) to (next state, symbols to write, moves),
    with one symbol and one move per tape.
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
    if "init" not in header or "accept" not in header:
        sys.exit("the program needs an init: and an accept: line")

    body = [line for line in lines if ":" not in line]
    if len(body) % 2 != 0:
        sys.exit("every rule needs two lines")
    if not body:
        sys.exit("the program has no rules")

    # The first rule tells how many tapes there are: state plus one symbol per tape.
    tapes = len(body[0].split(",")) - 1

    rules = {}
    for condition, action in zip(body[0::2], body[1::2]):
        condition = [x.strip() for x in condition.split(",")]
        action = [x.strip() for x in action.split(",")]
        if len(condition) != tapes + 1 or len(action) != 2 * tapes + 1:
            sys.exit(f"expected a rule for {tapes} tapes: {','.join(condition)} / {','.join(action)}")

        state, read = condition[0], tuple(condition[1:])
        next_state = action[0]
        write = tuple(action[1:tapes + 1])
        moves = action[tapes + 1:]
        if any(move not in MOVES for move in moves):
            sys.exit(f"moves must be <, > or -: {','.join(action)}")
        if (state, read) in rules:
            sys.exit(f"two rules for state {state} and symbols {','.join(read)}")
        rules[(state, read)] = (next_state, write, tuple(MOVES[move] for move in moves))

    accepting = {state.strip() for state in header["accept"].split(",")}
    return tapes, header["init"], accepting, rules


def show(cells, tape, head):
    """One tape, with its head in [ ]."""
    # Show every non-blank cell of this tape, and the head even if it stands on a blank.
    positions = [pos for (t, pos), symbol in cells.items() if t == tape and symbol != BLANK] + [head]
    text = ""
    for pos in range(min(positions), max(positions) + 1):
        symbol = cells.get((tape, pos), BLANK)
        text += f"[{symbol}]" if pos == head else symbol
    return text


def run(machine, word):
    """Runs the machine on the input word. Returns True if it accepts."""
    tapes, state, accepting, rules = machine
    cells = {}                   # (tape, position) -> symbol, everything else is blank
    for pos, symbol in enumerate(word):
        cells[(0, pos)] = symbol
    heads = [0] * tapes          # one head per tape, all start at position 0
    steps = 0

    while True:
        print(f"step={steps} state={state}")
        for tape in range(tapes):
            print(f"  tape {tape + 1}: {show(cells, tape, heads[tape])}")

        # Read one symbol per tape.
        read = tuple(cells.get((tape, heads[tape]), BLANK) for tape in range(tapes))

        # Accept in an accepting state, reject if no rule matches.
        rule = rules.get((state, read))
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

        # Apply the rule on every tape: write, move. Then change state.
        next_state, write, moves = rule
        for tape in range(tapes):
            cells[(tape, heads[tape])] = write[tape]
            heads[tape] += moves[tape]
        state = next_state
        steps += 1


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit('usage: python3 multituring.py <program> <input>   (use "" for an empty input)')
    program, word = sys.argv[1], sys.argv[2]
    run(load(open(program).read()), word)
