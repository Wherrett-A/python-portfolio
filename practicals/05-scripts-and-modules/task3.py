"""Write a program that takes a bunch of command-line arguments, and then prints
out the shortest. If there is more than one of the shortest length, any will do.
Hint: Don't overthink this. A good way to find the shortest is just to sort them."""

import sys

arguments = sys.argv
# removes file name from list
arguments.pop(0)

arguments.sort(key=len)
# if arguments is not None
if arguments:
    print(f'shortest argument: {arguments[0]}')
else:
    print('no arguments were given')
