"""The Unix grep command searches a file and outputs the lines in the file that
contain a certain pattern. Write an implementation of this. It will take two
command-line arguments: the first is the string to look for, and the second is the
file name. The output should be the lines in the file that contain the string."""
# substring is case-sensitive
import sys


def validate_args():
    if len(sys.argv) != 3:
        print('No argument was given or too many arguments given\n' +
              'use "task3.py <substring> <file address>"')
        return

    try:
        grep()
    except FileNotFoundError:
        print(f'File does not exist!\n'
              f'use "task3.py <substring> <file address>"')


def grep():
    with open(sys.argv[2], 'r') as file:
        content = file.readlines()
        # remove newlines from end of each line in list
        content = [line.rstrip() for line in content]
        for line in range(len(content)):
            if content[line].count(sys.argv[1]):
                print(f'<ln:{line+1}>|{content[line]}')
        print('Done.')


validate_args()
