#Choose a mode from a list: easy, medium, hard.
import argparse
parser = argparse.ArgumentParser(description = 'Choose a mode')
parser.add_argument('--mode', choices = ['easy', 'medium', 'hard'], required=True)
args = parser.parse_args()

print(f'You chose {args.mode} mode')