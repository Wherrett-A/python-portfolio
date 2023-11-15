"""Write a program that simulates the way in which a user might choose a password.
The program should prompt for a new password, and then prompt again. If the two
passwords entered are the same the program should say "Password Set" or
similar, otherwise it should report an error."""
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
    else:
        # if passwords do match, tell user 'Password Set'
        print('Password Set')
