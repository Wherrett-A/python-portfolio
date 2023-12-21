#!/usr/bin/env python3
# using msvcrt to get key presses for password input so the password is not visible while typing
import msvcrt


def passwd_input(string=''):
    """prints string then takes hidden input for passwords"""
    # prints the string and keeps the cursor on the same line while taking the input
    print(end='\r' + string)
    passwd = ''
    # listens for characters typed until enter is pressed
    while True:
        char = msvcrt.getch().decode("utf-8")
        # if enter is pressed the loop is broken
        if char == '\r':
            break
        passwd += char
    # blank print statement used to move cursor to next line
    print('')
    return passwd


def rot13(string):
    """performs a ROT13 encryption/ decryption"""
    rot13_translation = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
                                      'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm')
    return string.translate(rot13_translation)


def passwd_file(func, operator='r'):
    """opens the passwd.txt file with a given operator and performs a function on it"""
    with open('etc/passwd.txt', operator) as file:
        return func(file)


def get_passwd_entries(file):
    return file.read().split('\n')


def store(value):
    return lambda file: file.write(value)

