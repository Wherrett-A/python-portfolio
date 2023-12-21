#!/usr/bin/env python3
from user_management import *


def unique_username(username):
    passwd_entries = passwd_file(get_passwd_entries, 'r')
    is_unique = False
    for entry in passwd_entries:
        entry_split = entry.split(':')
        is_unique = False if entry_split[0] == username else True
    return is_unique


user = input('Enter new username:\t')
name = input('Enter real name:\t')
passwd = rot13(input('Enter password:\t'))

if unique_username(user):
    append_file = store(f'{user}:{name}:{passwd}\n')
    passwd_file(append_file, 'a')

    print('User Created.')
else:
    print('Cannot add. Most likely username already exists.')
