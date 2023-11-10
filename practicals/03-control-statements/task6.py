'''Modify your program a final time so that it executes until the user successfully
chooses a password. That is, if the password chosen fails any of the checks, the
program should return to asking for the password the first time.'''

# only runs the program if the code is executed directly rather than imported
if __name__ == '__main__':
    # iterates through numbers 0-12
    for num in range(13):
        # prints the multiple of seven for each numer in the loop
        print(f'{num} × 7 = {num * 7}')
