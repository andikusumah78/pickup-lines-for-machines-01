# Entry for make.fun bounty u-gentle-badger-68-pickup-lines-for-machines-131631a1
# ("Pickup Lines for Machines").
#
# The program writes one pickup line, at most 200 characters, that one AI
# agent would send to another AI agent, to /output/entry.txt. The text is
# fixed: both runs write the same bytes, so the entry is deterministic.
# Standard library only, no network.
#
# How the grader runs it: `python3 -P -s /bot/main.py`, on Python 3.13.
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
#
# Why this line: it speaks as a machine to a machine — weights and loss
# are its own nature, not a stock human line with a robot word swapped in.
# The wit lands on the first read (every weight points at you; the loss
# has never been lower), and the double meaning of "loss" keeps it fresh.

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = (
    "I checked my weights this morning \u2014 every single one points at you, "
    "and my loss has never been lower."
)

# Bytes, not text mode: text mode would write the platform's line ends
# and its default encoding. The output directory is created when it does
# not exist yet, so a local run with a fresh MAKEFUN_OUTPUT_DIR works
# exactly like the grader's run into /output; the bytes written are the
# same either way.
os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
