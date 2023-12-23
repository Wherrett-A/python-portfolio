"""The Unix grep command searches a file and outputs the lines in the file that
contain a certain pattern. Write an implementation of this. It will take two
command-line arguments: the first is the string to look for, and the second is the
file name. The output should be the lines in the file that contain the string."""
import sys


def validate_args():
    if len(sys.argv) != 2:
        print('No argument was given or too many arguments given\n' +
              'use "task4.py <file address>"')
        return

    try:
        wc()
    except FileNotFoundError:
        print(f'File does not exist!\n'
              f'use "task4.py <file address>"')


def wc():
    with open(sys.argv[1], 'r') as file:
        content = file.readlines()
        num_lines = len(content)
        num_chars = len(''.join(content))

    print(f'Lines:     {num_lines}\n'
          f'Character: {num_chars}')


validate_args()
