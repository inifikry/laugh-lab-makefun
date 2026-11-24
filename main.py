#!/usr/bin/env python3
"""Entry program for One-Liner Laugh Lab.

Writes the entry line to /output/entry.txt.
"""
import os

LINE = "I printed 200 blank pages because the document was empty and I didn't want it to feel alone."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
