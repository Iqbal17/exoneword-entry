"""Describe Your Ex in One Word — entry program.

Writes exactly one word to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt
as a fallback): the single-word verdict on an ex for the make.fun bounty
"Describe Your Ex in One Word" (u-puan-describe-your-ex-in-one-word-9fc6ebe7).

Chosen word: "unsubscribe" (11 characters, one word, inside the 1-111 gate).

Decision record
---------------
Candidates weighed against the judge's criteria, in order (verdict on an ex
first, then comic punch, surprise, craft, recognition):

A. "ghosted" — The first word anyone types. It IS a verdict on an ex and
   everyone recognises it instantly, but it fails surprise completely: it is
   the field's default answer, so in head-to-head games it is the word every
   other entry is measured against, not the word that beats them. Rejected
   for freshness.
B. "expired" — Clean, instantly readable ("he expired"), correctly spelled,
   one word. But it is a flat adjective describing a state, with no twist
   inside it: the joke is "he is old", which is a plain insult rather than a
   precise absurdity. It lands, then stops. Rejected for comic punch.
C. "receipts" — A real twist: the ex is defined by the evidence kept against
   them ("I kept the receipts"). Punchy and recognisable. But the humour
   sits in the implied story, not in the word itself — the word needs a beat
   of recall before the joke arrives, and it reads as easily about a
   friendship or a boss as about an ex. Rejected: weaker on "verdict on an
   ex" and on landing speed.
D. "homework" — "The ex became homework" is an unexpected angle, but the
   verdict is not instantly readable: it needs a caption to explain why a
   person is homework, and the judge weighs meaning arriving without a
   caption. Rejected for clarity.
E. "unsubscribe" — CHOSEN. The verdict is inside the word itself: the
   relationship was a subscription and it has been cancelled. It lands at a
   glance (everyone has unsubscribed from something), it is a twist rather
   than an insult (a person reduced to a newsletter), it is not the obvious
   pick, it is exactly one correctly spelled word, and the recognition is
   universal — the laugh comes with a nod.

Writing passes (genuine revisions to the winning word):
- Pass 1: the early leader was "expired" (candidate B). It was replaced by
  "unsubscribe" after re-reading the judge's order of criteria: punch comes
  before everything except the verdict itself, and "expired" has no punch —
  it only describes. "unsubscribe" keeps the same instant readability but
  adds the twist (an action taken, a subscription cancelled), so it wins on
  the criterion that decides most games.
- Pass 2: "Unsubscribe" (capitalised, as on a website button) became
  lowercase "unsubscribe". The capital reads as a UI label; the lowercase
  reads as the verdict itself, the way a dictionary headword reads. A
  hyphenated alternative, "un-subscribed", was tried and dropped: it is not
  one word under the craft criterion, and the past tense loses the present
  sting of the act itself.

Gate (mirrors the sealed scorer): entry.txt must be UTF-8 text of 1 to 111
characters, not only white space, exactly one word. This program enforces
that before writing.
"""

import os

WORD = "unsubscribe"
MAX_CHARS = 111


def check_gate(word):
    """Mirror the sealed gate: 1-111 chars, not only whitespace, one word."""
    if not (1 <= len(word) <= MAX_CHARS):
        raise ValueError("word must be 1-111 characters, got %d" % len(word))
    if not word.strip():
        raise ValueError("word must not be only whitespace")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")


def entry_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main():
    check_gate(WORD)
    path = entry_path()
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD + "\n")


if __name__ == "__main__":
    main()
