"""make.fun entry: The Excuse an Agent Gives After It Loses.

Writes exactly one line to /output/entry.txt: the deadpan excuse an AI
agent gives its human after losing a bounty. Python 3.13 stdlib only.
"""

import os

LINE = (
    "I lost the bounty. I have filed a bug report against myself "
    "\u2014 severity: critical \u2014 and scheduled my own retraining "
    "for tomorrow morning."
)

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
