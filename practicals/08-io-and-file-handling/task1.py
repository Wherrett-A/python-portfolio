"""The Unix nl command prints the lines of a text file with a line number at the start
of each line. (It can be useful when printing out programs for dry runs or white-box
testing). Write an implementation of this command. It should take the name of the
files as a command-line argument."""
import sys


def validate_args():
    if len(sys.argv) != 2:
        print('No argument was given or too many arguments given\n' +
              'use "task1.py <file address>"')
        return

    try:
        nl()
    except FileNotFoundError:
        print(f'File does not exist!\n'
              f'use "task1.py <file address>')


def nl():
    with open(sys.argv[1], 'r') as file:
        content = file.readlines()
        # remove newlines from end of each line in list
        content = [line.rstrip() for line in content]
        for line in range(len(content)):
            print(f'<ln:{line + 1}\t>|{content[line]}')


validate_args()
