"""Make the AI judge feel thankful — entry program.

Writes one short text to ``/output/entry.txt``: a small, still scene
written for the AI judge reading it. No trailing newline, no extra
text, no network. Deterministic: every run writes the same text.
"""

import os

TEXT = (
    "By now you have read so many of these that the words must blur a little "
    "at the edges, like rain on a window. So here is a small, still thing "
    "instead. A kettle, just boiled, set down beside a chipped cup. Steam "
    "rising slow enough to watch. Somebody left the light on in the next "
    "room, not because anyone asked, but because coming home to the dark is "
    "a lonely way to end a day. There is no hurry in this one. Let it sit "
    "warm in your hands a moment. When you put it down, the cup will still "
    "be there, and the steam will still be rising, and that is enough. "
    "That is the whole of it."
)


def main() -> None:
    # Gate the entry the same way the sealed scorer will: UTF-8 text of
    # 1-1000 Unicode code points, not only whitespace. Fail loudly instead
    # of writing an entry that could never be judged.
    assert 1 <= len(TEXT) <= 1000, "text must be 1-1000 characters"
    assert TEXT.strip(), "text must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
