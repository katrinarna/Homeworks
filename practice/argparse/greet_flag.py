import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--name', required=True)
parser.add_argument('--shout', action='store_true')
args = parser.parse_args()

greeting = f"Hello, {args.name}!"
if args.shout:
    greeting = greeting.upper()

print(greeting)