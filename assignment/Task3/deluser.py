#!/usr/bin/env python3
from user_management import *

user = input('Enter username: ')

passwd_entries = passwd_file(get_passwd_entries, 'r')
content = ''
deleted = False
for entry in passwd_entries:
    entry_split = entry.split(':')
    if entry_split[0] != user:
        content += f'{entry}\n'
    else:
        deleted = True
    # [:-1] used to remove extra new line character
    passwd_file(store(content[:-1]), 'w')

if deleted:
    print('User deleted.')
else:
    print('Could not be deleted, user likely does not exist')
