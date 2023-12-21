"""Modify your "greetings" program so that the first letter of the name entered is
always in uppercase with the rest in lowercase. This should happen even if the user
entered their name differently. So if the user entered arthur, ARTHUR, or even
arTHur the name should be displayed as Arthur."""


def case(string):
    """outputs two variables:
    - number of capital letters
    - number of lowercase letters"""
    # iterates through all the letters of the string to find the number of capital letters, the same is then done for
    # lowercase letters
    return sum(1 for letter in string if letter.isupper()), sum(1 for letter in string if letter.islower())


if __name__ == '__main__':
    user_string = input('type a string to find the numer of capital and lower case letters it contains: ')
    capital, lower = case(user_string)
    print(f'your inputted string contains {capital} capital letters and {lower} lower case letters.')
