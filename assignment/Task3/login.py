#!/usr/bin/env python3
from user_management import *

user = input('User:\t  ')
passwd = rot13(passwd_input('Password: '))

passwd_entries = passwd_file(get_passwd_entries, 'r')

logged_in = False

for entry in passwd_entries:
    entry_split = entry.split(':')
    if entry_split[0] == user and entry_split[2] == passwd:
        logged_in = True
        break

if logged_in:
    print('Access granted.')
else:
    print('Access denied.')
