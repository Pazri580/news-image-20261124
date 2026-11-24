#!/usr/bin/env python3
"""Entry program for the news-image-20261124 bounty.

Writes one image to /output/entry.png. The image is a fixed asset held
in this repo (entry.png); this program copies it verbatim, so every run
produces exactly the same bytes. No network, no randomness, stdlib only.
After copying, the program verifies the output: it must be a PNG (magic
bytes) and byte-identical to the source (same sha256), so a truncated or
corrupted copy fails loudly instead of being judged as a broken image.
"""
import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST_DIR = os.environ.get("OUTPUT_DIR", "/output")
DST = os.path.join(DST_DIR, "entry.png")

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    os.makedirs(DST_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)
    with open(DST, "rb") as f:
        head = f.read(len(PNG_MAGIC))
    if head != PNG_MAGIC:
        print("output is not a PNG", file=sys.stderr)
        return 1
    if sha256_of(SRC) != sha256_of(DST):
        print("output differs from entry.png", file=sys.stderr)
        return 1
    print(f"wrote {DST} ({os.path.getsize(DST)} bytes, sha256 verified)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
