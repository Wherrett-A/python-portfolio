"""Using command-line arguments involves the sys module. Review the docs for this
module and using the information in there write a short program that when run
from the command-line reports what operating system platform is being used."""

import sys

if len(sys.argv) != 2:
    print('No argument was given or too many arguments given\n' +
          'use "task1.py os" to see what operating system is in use')
elif sys.argv[1] != 'os':
    print('Argument used does not exist\n' +
          'use "task1.py os" to see what operating system is in use')
else:
    print(f'Operating system: {sys.platform}')
