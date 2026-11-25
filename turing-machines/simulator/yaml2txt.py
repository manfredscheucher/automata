"""yaml2txt: converts a program from the YAML format of turingmachine.io
to the turingmachinesimulator.com format, so it runs there and in minituring.py.

Usage:   python3 yaml2txt.py <program.yaml>  > <program>.txt
Example: python3 yaml2txt.py ../examples/palindrome/binary-palindrome-simplified.yaml

Differences between the two formats:
- The blank (often ' ') becomes _.
- turingmachine.io has no accepting states. If the file has a comment
  "Accepting states: ..." (as txt2yaml.py writes it), those are used.
  Otherwise all states without rules accept, except one called reject.

Only handles the part of YAML that turingmachine.io programs use, so no YAML
library is needed.
"""
import os
import re
import sys

MOVES = {"L": "<", "R": ">"}


def strip_comment(line):
    """Removes a # comment that is not inside quotes."""
    quote = None
    for i, c in enumerate(line):
        if c in "'\"":
            quote = None if quote == c else (quote or c)
        elif c == "#" and quote is None and (i == 0 or line[i - 1] == " "):
            return line[:i].rstrip(), line[i + 1:].strip()
    return line.rstrip(), None


def scalar(text):
    """A YAML scalar: '...' or "..." or plain text."""
    text = text.strip()
    if len(text) >= 2 and text[0] == text[-1] and text[0] in "'\"":
        return text[1:-1]
    return text


def split_items(text, raw=False):
    """Splits "a, 'b', c" at commas outside quotes and outside [ ] and { }."""
    items, current, quote, depth = [], "", None, 0
    for c in text:
        if c in "'\"":
            quote = None if quote == c else (quote or c)
        elif quote is None and c in "[{":
            depth += 1
        elif quote is None and c in "]}":
            depth -= 1
        if c == "," and quote is None and depth == 0:
            items.append(current)
            current = ""
        else:
            current += c
    items.append(current)
    return [x.strip() for x in items] if raw else [scalar(x) for x in items]


def split_rule(text):
    """Splits "<symbols>: <action>" at the colon after the symbols."""
    text = text.strip()
    if text.startswith("["):
        end = text.index("]") + 1
        return text[:end], text[end:].lstrip()[1:]
    if text[0] in "'\"":
        end = text.index(text[0], 1) + 1
        return text[:end], text[end:].lstrip()[1:]
    key, _, value = text.partition(":")
    return key, value


def parse_symbols(key):
    """'a' or [a, b, ' '] -> list of symbols."""
    key = key.strip()
    if key.startswith("["):
        return split_items(key[1:-1])
    return [scalar(key)]


def parse_action(value, synonyms):
    """R, L, {write: x, L}, {R: state} or a synonym -> (write or None, move, next state or None)."""
    value = value.strip()
    if value in synonyms:
        return parse_action(synonyms[value], synonyms)
    if value in MOVES:
        return None, MOVES[value], None
    assert value.startswith("{") and value.endswith("}"), value
    write, move, next_state = None, None, None
    for item in split_items(value[1:-1]):
        key, _, val = item.partition(":")
        key, val = key.strip(), val.strip()
        if key == "write":
            write = scalar(val)
        else:
            move = MOVES[key]
            next_state = scalar(val) if val else None
    assert move, value
    return write, move, next_state


def parse(text):
    """Parses a program. Returns its name, settings, states, rules and comments.

    Also reads the example files of turing-machine-viz, where the program sits
    in a "source code: |" block.
    """
    lines = text.split("\n")
    name = None
    if "source code: |" in lines:
        name = next(line.split(":", 1)[1].strip() for line in lines if line.startswith("name:"))
        body = []
        for line in lines[lines.index("source code: |") + 1:]:
            if line and not line.startswith("  "):
                break
            body.append(line[2:])
    else:
        body = lines

    settings, synonyms, table, states = {}, {}, {}, []
    header, notes = [], {}               # comments before the table and per state
    pending = []                         # comment lines waiting for the next state
    section, state = None, None
    for raw in body:
        line, comment = strip_comment(raw)
        indent = len(raw) - len(raw.lstrip())
        if not line.strip():                       # a comment line or a blank line
            pending.append(raw.strip()[1:].rstrip() if raw.strip() else "")
            continue
        key, value = split_rule(line)
        if indent == 0:
            if section != "table":
                header += pending
                pending = []
            section = None if value.strip() else key
            if value.strip():
                settings[key] = value
                if key == "input" and comment:
                    settings["try"] = comment
        elif section == "synonyms":
            synonyms[key.strip()] = value.strip()
        elif section == "table" and indent == 2:
            state = key.strip()
            states.append(state)
            table[state] = []
            notes[state] = pending + ([" " + comment] if comment else [])
            pending = []
            if value.strip().startswith("{"):   # whole state on one line: {sym: action, ...}
                for item in split_items(value.strip()[1:-1], raw=True):
                    k, v = split_rule(item)
                    for symbol in parse_symbols(k):
                        table[state].append((symbol, parse_action(v, synonyms), []))
        elif section == "table" and indent == 4:
            # Comments above a rule and behind it belong to that rule; with several
            # symbols they are written only once, above the first one.
            rule_notes = pending + ([" " + comment] if comment else [])
            pending = []
            for i, symbol in enumerate(parse_symbols(key)):
                table[state].append((symbol, parse_action(value, synonyms), rule_notes if i == 0 else []))
    footer = pending                     # comments after the table
    return name, settings, states, table, header, notes, footer


def comment_block(lines):
    """Comment lines as // lines, without blank lines at the start and end."""
    while lines and not lines[0].strip():
        lines = lines[1:]
    while lines and not lines[-1].strip():
        lines = lines[:-1]
    return [("//" + line).rstrip() for line in lines]


def accepting_states(states, table, header):
    """The states from an "Accepting states: ..." comment, or else all states
    without rules except reject."""
    for line in header:
        match = re.match(r"\s*Accepting states: (.*?)\.", line)
        if match:
            return [s.strip() for s in match.group(1).split(",")]
    return [s for s in states if not table[s] and s != "reject"]


def write_program(name, settings, states, table, header, notes, footer, intro):
    """The program in the turingmachinesimulator.com format.

    intro: comment lines for the top, for example where the program comes from.
    """
    blank = scalar(settings.get("blank", "' '"))

    def sym(s):
        return "_" if s == blank else s

    accepting = accepting_states(states, table, header)
    out = [f"// {name}"] + intro + [f"// The blank {blank!r} is written as _ here."]
    if "input" in settings:
        tries = f" ({settings['try']})" if "try" in settings else ""
        out.append(f"// Example input: {scalar(settings['input'])}{tries}")
    else:
        out.append("// Example input: none, start with an empty tape.")
    block = comment_block(header)
    if block:
        out += ["//"] + block
    out += ["", f"name: {name}", f"init: {scalar(settings['start state'])}"]
    out.append(f"accept: {', '.join(accepting)}" if accepting else "accept: none")
    out.append("")
    for state in states:
        block = comment_block(notes[state])
        if block:
            out += block
        for symbol, (write, move, next_state), rule_notes in table[state]:
            out += comment_block(rule_notes)
            out.append(f"{state},{sym(symbol)}")
            out.append(f"{next_state or state},{sym(write if write is not None else symbol)},{move}")
            out.append("")
    block = comment_block(footer)
    if block:
        out += block
    return "\n".join(out).rstrip() + "\n"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: python3 yaml2txt.py <program.yaml>")
    path = sys.argv[1]
    name, *rest = parse(open(path).read())
    name = name or os.path.splitext(os.path.basename(path))[0]
    print(write_program(name, *rest, ["// Converted from the turingmachine.io format with yaml2txt.py."]), end="")
