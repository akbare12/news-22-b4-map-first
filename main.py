#!/usr/bin/env python3
"""Copy entry.png to the output directory (stdlib only, no network).

Verifies the copy byte for byte (size + sha256) so a corrupt or
truncated write is never submitted silently.
"""
import hashlib
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    os.makedirs(OUT, exist_ok=True)
    dst = os.path.join(OUT, "entry.png")
    shutil.copyfile(SRC, dst)
    if os.path.getsize(SRC) != os.path.getsize(dst):
        raise SystemExit("size mismatch after copy")
    if sha256(SRC) != sha256(dst):
        raise SystemExit("sha256 mismatch after copy")


if __name__ == "__main__":
    main()
