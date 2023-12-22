"""Write a program that takes the name of a file as a command-line argument, and
creates a backup copy of that file. The backup should contain an exact copy of the
contents of the original and should, obviously, have a different name."""

import sys

if len(sys.argv) != 2:
    print('not enough or too many arguments used\n'
          'should be one argument with file address')
else:
    try:
        with open(sys.argv[1], 'r') as file:
            content = file.read()
        with open(f'{sys.argv[1]}.backup', 'x') as backup:
            backup.write(content)
        print('Backup created.')
    except FileNotFoundError:
        print(f'file "{sys.argv[1]}" does not exist')
    except FileExistsError:
        print(f'delete previous backup before creating a new one')
