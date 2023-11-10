'''Modify your program a final time so that it executes until the user successfully
chooses a password. That is, if the password chosen fails any of the checks, the
program should return to asking for the password the first time.'''
# imports inbuilt 'getpass' module to hide password input
from getpass import getpass

# only runs the program if the code is executed directly rather than imported
if __name__ == '__main__':
    # list of common passwords
    BAD = ['password', 'password123', '12345678', '11111111', 'iloveyou', 'football', 'qwertyuiop']

    print('~~ YOU WILL NOT SEE YOUR INPUT WHILE TYPING IN THE INPUT FIELD ~~')

    # loops the code  until password meets the criteria and a break is triggered
    while True:
        # uses getpass to take password as input (getpass only works in the terminal)
        pwd = getpass('Enter Password: ')
        pwd_repeated = getpass('Re-enter Password: ')

        if pwd != pwd_repeated:
            # if passwords do not match, print error to the console
            print('Passwords do not match.')
        elif 8 > len(pwd) or len(pwd) > 12:
            # if length is not in between 8 & 12 characters, print error
            print('Password must be between 8 and 12 characters.')
        elif pwd in BAD:
            # if password is in the list, print error
            print('you have entered a common password')
        else:
            # if passwords do match, tell user 'Password Set' and break from the loop
            print('Password Set.')
            break
