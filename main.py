"""One Emoji, One Dream Vacation — entry.

A single emoji as a wordless postcard: a penguin, standing in for an
Antarctic expedition — the far edge of the world, icebergs, and a colony
of penguins. Specific, surprising, and instantly readable across any
culture or screen. No words needed; the trip is the picture.

Running this program writes the entry emoji to /output/entry.txt.
"""

import os

ENTRY_EMOJI = "🐧"  # One emoji only — the whole entry, no words.


def main() -> None:
    """Write the entry emoji to /output/entry.txt (UTF-8)."""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_EMOJI)


if __name__ == "__main__":
    main()
