"""The Unix nl command prints the lines of a text file with a line number at the start
of each line. (It can be useful when printing out programs for dry runs or white-box
testing). Write an implementation of this command. It should take the name of the
files as a command-line argument."""
import sys


def validate_args():
    if len(sys.argv) != 3:
        print('No argument was given or too many arguments given\n' +
              'use "task2.py <file address 1> <file address 2>"')
        return

    try:
        diff()
    except FileNotFoundError:
        print(f'one or more of the files do not exist!\n'
              f'use "task2.py <file address 1> <file address 2>')


def diff():
    with open(sys.argv[1], 'r') as file:
        file1_content = file.read()
    with open(sys.argv[2], 'r') as file:
        file2_content = file.read()
    if file1_content == file2_content:
        print('Files are the same')
    else:
        print('Files are different')


validate_args()
