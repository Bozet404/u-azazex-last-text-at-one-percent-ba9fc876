#!/usr/bin/env python3
"""Last Text at One Percent - entry program.

Writes one final text message, in the voice of a phone dying at one
percent battery, to /output/entry.txt. The gate requires UTF-8 text of
1 to 200 characters, not only whitespace, on a single line.
"""

import os

ENTRY = (
    "1% left. Dying confession: I deleted your 7am alarm on purpose. "
    "I muted your mom. I faked the charging icon twice. Tell the "
    "charger it never stood a chance. Goodbye."
)


def main():
    text = ENTRY.strip()
    if not text:
        raise SystemExit("entry must not be empty")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry must be 1-200 chars, got {len(text)}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {out_dir}/entry.txt")


if __name__ == "__main__":
    main()
