import argparse

#Create a script that takes a --name argument and prints Hello, <name>!
def parse_arguments():

    parser = argparse.ArgumentParser(description = 'Script that greets user')

    parser.add_argument('--name', type=str, default = 'world', help= 'the name of person to greet')

    return parser.parse_args()

def main():
    args = parse_arguments()
    print(f'Hello, {args.name}')

if __name__ == '__main__':
    main()