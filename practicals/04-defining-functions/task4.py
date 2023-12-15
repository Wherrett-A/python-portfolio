"""When processing data it is often useful to remove the last character from some
input (it is often a newline). Write and test a function that takes a string parameter
and returns it with the last character removed. (If the string contains one or fewer
characters, return it unchanged.)"""


# defines process function
def process(string):
    """returns string with the last character removed if the string has more than 1 character otherwise returns the
    string"""
    return string[:-1] if len(string) > 1 else string


# only runs the program if the code is executed directly rather than imported
if __name__ == '__main__':
    # takes a string from the user to pass to process function
    user_string = input('type a string: ')
    # prints returned string from the processed function after the users string has been entered
    print(process(user_string))
