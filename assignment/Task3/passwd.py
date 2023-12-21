#!/usr/bin/env python3
from user_management import *

user = input('User:\t\t  ')
current_passwd = rot13(passwd_input('Current Password: '))
new_passwd = rot13(passwd_input('New Password:\t  '))
confirm = rot13(passwd_input('confirm:\t  '))

passwd_entries = passwd_file(get_passwd_entries, 'r')
content = ''
passwd_correct = False
for entry in passwd_entries:
    entry_split = entry.split(':')
    if entry_split[0] == user and entry_split[2] == current_passwd:
        content += f'{entry_split[0]}:{entry_split[1]}:{new_passwd}\n'
        passwd_correct = True
    else:
        content += f'{entry}\n'

if new_passwd == confirm and passwd_correct:
    # [:-1] used to remove extra new line character
    passwd_file(store(content[:-1]), 'w')
    print('Password changed if user exists.')
elif not passwd_correct:
    print('Current password is incorrect.')
else:
    print('New passwords do not match.')