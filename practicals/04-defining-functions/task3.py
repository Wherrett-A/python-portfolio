"""Modify your "greetings" program so that the first letter of the name entered is
always in uppercase with the rest in lowercase. This should happen even if the user
entered their name differently. So if the user entered arthur, ARTHUR, or even
arTHur the name should be displayed as Arthur."""

# only runs the program if the code is executed directly rather than imported
if __name__ == '__main__':
    # prompts user to enter there name then stores it in 'name' variable
    name = input('What is your name?')
    # prints name in title case using name.title() along with a cheery message
    print(f'Hello, {name.title()}. Good to meet you!')
