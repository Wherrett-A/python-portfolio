"""Modify your "greetings" program so that the first letter of the name entered is
always in uppercase with the rest in lowercase. This should happen even if the user
entered their name differently. So if the user entered arthur, ARTHUR, or even
arTHur the name should be displayed as Arthur."""


# defines case function
def case(string):
    """outputs two variables:
    - number of capital letters
    - number of lowercase letters"""
    # iterates through all the letters of the string to find the number of capital letters, the same is then done for
    # lowercase letters
    return sum(1 for letter in string if letter.isupper()), sum(1 for letter in string if letter.islower())


# only runs the program if the code is executed directly rather than imported
if __name__ == '__main__':
    # takes a string from the user to pass through the function
    user_string = input('type a string to find the numer of capital and lower case letters it contains: ')
    # passes string to case function and stores returned values as 'capital' and 'lower' containing the number of
    # capital letters and lower case letters respectively
    capital, lower = case(user_string)
    # prints number of upper and lower case letters to the console
    print(f'your inputted string contains {capital} capital letters and {lower} lower case letters.')
