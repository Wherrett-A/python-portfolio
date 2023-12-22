"""Write a program that takes a URL as a command-line argument and reports
whether or not there is a working website at that address."""

import sys
import urllib.error
import urllib.request

if len(sys.argv) != 2:
    print('not enough or too many arguments used')
else:
    try:
        request = urllib.request.urlopen(f'http://{sys.argv[1]}')
        print(f'working website exists at address "{sys.argv[1]}"')
    except urllib.error.HTTPError or urllib.error.URLError as error:
        print(f'working website does not exist at address "{sys.argv[1]}"\n'
              f'error returned -> {error.code}: {error.reason}')
