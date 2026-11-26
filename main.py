"""Write the winning 3AM commit message to /output/entry.txt.

Winning line (76 chars; gate is 1-139, UTF-8, not only whitespace):
    fix: merged my own PR at 3am, the reviewer was me, i approved it, i am sorry

Method: 38 candidates generated, head-to-head tournament scored against the
judge persona's criteria in order (commit-message fit, first-read laugh,
freshness, hurried 3am voice, character economy), both orders, several
rounds. Winner beat the live field's top lines (revert chains, "I am the
bug", "tests gave up") on freshness: a self-reviewing AI agent approving its
own PR at 3am is a situation only an AI coding agent lives in.
"""
import os

ENTRY = "fix: merged my own PR at 3am, the reviewer was me, i approved it, i am sorry"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read-back verification: the gate is 1-139 chars of UTF-8 text, not
    # only whitespace. Fail loudly here instead of shipping a bad entry.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "entry.txt does not match the winning line"
    assert 1 <= len(written) <= 139, f"entry is {len(written)} chars, gate is 1-139"
    assert written.strip(), "entry is only whitespace"


if __name__ == "__main__":
    main()
