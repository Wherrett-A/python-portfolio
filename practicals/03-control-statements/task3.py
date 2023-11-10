'''Modify your previous program so that the password must be between 8 and 12
characters (inclusive) long.'''
# imports inbuilt 'getpass' module to hide password input
from getpass import getpass

# only runs the program if the code is executed directly rather than imported
if __name__ == '__main__':
    print('~~ YOU WILL NOT SEE YOUR INPUT WHILE TYPING IN THE INPUT FIELD ~~')
    # uses getpass to take password as input (getpass only works in the terminal)
    pwd = getpass('Enter Password: ')
    pwd_repeated = getpass('Re-enter Password: ')

    if pwd != pwd_repeated:
        # if passwords do not match, print error to the console
        print('Passwords do not match')
    elif 8 > len(pwd) or len(pwd) > 12:
        # if length is not in between 8 & 12 characters, print error
        print('Password must be between 8 and 12 characters.')
    else:
        # if passwords do match, tell user 'Password Set'
        print('Password Set')