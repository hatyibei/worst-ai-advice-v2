"""Write this entry's text to the make.fun output directory.

The sealed scorer reads /output/entry.txt, so all this program has to do
is copy the entry file next to it into $MAKEFUN_OUTPUT_DIR, byte for byte.
"""

import os

ENTRY_NAME = "entry.txt"
CHUNK_SIZE = 65536


def copy_entry(src, dst):
    """Copy a file in binary chunks, so the bytes land exactly as stored."""
    with open(src, "rb") as fin, open(dst, "wb") as fout:
        while True:
            chunk = fin.read(CHUNK_SIZE)
            if not chunk:
                break
            fout.write(chunk)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, ENTRY_NAME)
    dst = os.path.join(out_dir, ENTRY_NAME)
    copy_entry(src, dst)


if __name__ == "__main__":
    main()
