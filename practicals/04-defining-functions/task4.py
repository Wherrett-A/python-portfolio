"""When processing data it is often useful to remove the last character from some
input (it is often a newline). Write and test a function that takes a string parameter
and returns it with the last character removed. (If the string contains one or fewer
characters, return it unchanged.)"""


def process(string):
    """returns string with the last character removed if the string has more than 1 character otherwise returns the
    string"""
    return string[:-1] if len(string) > 1 else string


if __name__ == '__main__':
    user_string = input('type a string: ')
    print(process(user_string))
