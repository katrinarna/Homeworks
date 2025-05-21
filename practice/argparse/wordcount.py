#Pass a filename as a positional argument and count how many words are in it.

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename')
args = parser.parse_args()

with open(args.filename, 'r') as file:
    text = file.read()
    words = text.split()
    print(f"Total words: {len(words)}")
