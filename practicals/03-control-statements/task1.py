"""Modify your greeting program so that if the user does not enter a name (i.e. they
just press enter), the program responds "Hello, Stranger!". Otherwise it should print
a greeting with their name as before"""

# only runs the program if the code is executed directly rather than imported
if __name__ == '__main__':
    # prompts user to enter there name then stores it in 'name' variable
    name = input('What is your name?')

    # checks if variable 'name' has a value to decide which message to print
    if name:
        # uses inbuilt print function to print a cheery message
        print(f'Hello, {name}. Good to meet you!')
    else:
        # uses inbuilt print function to print a cheery message
        print('Hello, stranger. Good to meet you!')
