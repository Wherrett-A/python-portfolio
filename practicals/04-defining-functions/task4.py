"""When processing data it is often useful to remove the last character from some
input (it is often a newline). Write and test a function that takes a string parameter
and returns it with the last character removed. (If the string contains one or fewer
characters, return it unchanged.)"""

# only runs the program if the code is executed directly rather than imported
if __name__ == '__main__':
    # takes a string from the user
    user_string = input('type a string: ')
    # prints the users inputted string with the last character removed
    print(user_string[:-1])
