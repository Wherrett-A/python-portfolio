"""The Unix grep command searches a file and outputs the lines in the file that
contain a certain pattern. Write an implementation of this. It will take two
command-line arguments: the first is the string to look for, and the second is the
file name. The output should be the lines in the file that contain the string."""
import sys
import re


def get_wordlist():
    with open('dict/words', 'r') as wordlist:
        words = wordlist.read()
        return re.split('\s', words)  # split content into list by whitespace


def validate_args():
    if len(sys.argv) != 2:
        print('No argument was given or too many arguments given\n' +
              'use "task5.py <file address>"')
        return

    try:
        spell()
    except FileNotFoundError:
        print(f'File does not exist!\n'
              f'use "task5.py <file address>"')


def spell():
    wordlist = get_wordlist()
    with open(sys.argv[1], 'r') as file:
        content = file.read().lower()
        content_words = list(set(re.split('\W', content)))  # split content into list by non-words
    for word in content_words:
        if not wordlist.count(word):
            print(word)
    print('Done.')


validate_args()
