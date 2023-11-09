'''Last week you wrote a program that printed out a cheery greeting including your
name. Take a copy of it, and modify it so that the user enters their name at the
keyboard, and then receives a greeting'''

# only runs the program if the code is executed directly rather than imported
if __name__ == '__main__':
    # prompts user to enter there name then stores it in 'name' variable
    name = input('What is your name?')
    # uses inbuilt print function to print a cheery message
    print(f'Hello, {name}. Good to meet you!')
