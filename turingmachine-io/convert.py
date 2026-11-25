"""Converts the turingmachine.io examples (YAML, from turing-machine-viz) to the
turingmachinesimulator.com format.

Usage: python3 convert.py <turing-machine-viz>/src/examples <output folder>

Only handles the small part of YAML the examples use, so no YAML library is needed.
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


def convert(path):
    """Parses one example. Returns its name, settings, states, rules and comments."""
    lines = open(path).read().split("\n")
    name = next(l.split(":", 1)[1].strip() for l in lines if l.startswith("name:"))
    start = lines.index("source code: |") + 1
    body = []
    for line in lines[start:]:
        if line and not line.startswith("  "):
            break
        body.append(line[2:])

    settings, synonyms, table, states = {}, {}, {}, []
    header, notes, footer = [], {}, []   # comments before the table, per state, after the table
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
                        table[state].append((symbol, parse_action(v, synonyms), None))
        elif section == "table" and indent == 4:
            notes[state] += pending
            pending = []
            for symbol in parse_symbols(key):
                table[state].append((symbol, parse_action(value, synonyms), comment))
    footer = pending
    return name, settings, states, table, header, notes, footer


def comment_block(lines):
    """Comment lines as // lines, without blank lines at the start and end."""
    while lines and not lines[0].strip():
        lines = lines[1:]
    while lines and not lines[-1].strip():
        lines = lines[:-1]
    return [("//" + l).rstrip() for l in lines]


def write_program(name, settings, states, table, header, notes, footer, source):
    blank = scalar(settings.get("blank", "' '"))

    def sym(s):
        return "_" if s == blank else s

    # States without rules are where the machine halts; all of them accept except "reject".
    accepting = [s for s in states if not table[s] and s != "reject"]
    out = [f"// {name}",
           f"// Ported from the turingmachine.io example {source}",
           "// by Andy Li, https://github.com/aepsilon/turing-machine-viz (BSD 3-Clause, see LICENSE).",
           f"// The blank {blank!r} is written as _ here."]
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
        for symbol, (write, move, next_state), comment in table[state]:
            if comment:
                out.append(f"// {comment}")
            out.append(f"{state},{sym(symbol)}")
            out.append(f"{next_state or state},{sym(write if write is not None else symbol)},{move}")
            out.append("")
    block = comment_block(footer)
    if block:
        out += block
    return "\n".join(out).rstrip() + "\n"


if __name__ == "__main__":
    src, dst = sys.argv[1], sys.argv[2]
    for f in sorted(os.listdir(src)):
        if not f.endswith(".yaml") or f.startswith("_"):
            continue
        parsed = convert(os.path.join(src, f))
        # binaryIncrement -> binary-increment.txt, divisibleBy3Base10 -> divisible-by-3-base-10.txt
        out = re.sub(r"(?<=[a-z])(?=[A-Z0-9])|(?<=[0-9])(?=[A-Z])", "-", f[:-5]).lower() + ".txt"
        open(os.path.join(dst, out), "w").write(write_program(*parsed, f[:-5]))
        print(out, len(parsed[2]), "states", sum(len(r) for r in parsed[3].values()), "rules")
