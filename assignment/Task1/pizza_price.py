#!/usr/bin/env python3
def loop_program():
    # loops program until there is a KeyboardInterrupt
    while True:
        run()


def run():
    # defines a greeting to be printed when program starts
    greeting = 'BPP Pizza Price Calculator'

    # prints the greeting defined above underlined with '=' character
    print(greeting + '\n' + '=' * len(greeting) + '\n')

    # runs the take_inputs function and stores returned price in price variable
    value = take_inputs()

    # prints the total price to 2dp using :.2f format
    # unless take_inputs returned a string in which case the string is printed
    print(f'Total Price: £{value:.2f}.') if not isinstance(value, str) else print(value)


def take_inputs():

    # collects user inputs
    pizzas = input('How many pizzas ordered? ')
    delivery = input('Is delivery required?(y/n) ')
    tuesday = input('Is it a Tuesday?(y/n) ')
    app_used = input('Did the customer use the app?(y/n) ')
    # prints a new line for aesthetic
    print('\n')

    # returns value of valid_input function which is passed the users inputs as kwargs
    return valid_input(pizzas=pizzas, delivery=delivery, tuesday=tuesday, app_used=app_used)


def valid_input(**options):
    # uses guard clause format to validate inputs
    # if the number of pizzas the user entered is not an integer, the function returns an error
    if not options['pizzas'].isnumeric():
        return 'Number of pizzas should be an integer.'
    # if the user entered a negative number of pizzas, the function returns an error
    if int(options['pizzas']) < 1:
        return 'Numer of pizzas should be a positive integer.'
    # iterates through delivery, tuesday, and app_used inputs to check values are either 'y' or 'n'
    # if they are not valid an error is returned
    for value in ['delivery', 'tuesday', 'app_used']:
        # checks each input is either 'y' or 'n', case-insensitive
        if options[value].upper() != 'Y' and options[value].upper() != 'N':
            return 'All inputs other than the number of pizzas should be "y" or "n".'
    # returns value of cost function which calculates cost of the pizzas using the validated inputs
    return cost(options)


def cost(options):
    # calculates raw cost of the pizzas excluding delivery and any discounts
    pizzas = 12 * int(options['pizzas'])
    # delivery variable stores cost of delivery (2.5 or 0) depending on whether delivery is required
    delivery = 2.5 if options['delivery'].upper() == 'Y' else 0
    # tuesday variable holds value of multiplier to determine if tuesday discount should be applied
    # 0.5 if it is tuesday otherwise value is 1
    tuesday = 0.5 if options['tuesday'].upper() == 'Y' else 1
    # app_used variable holds value of multiplier to determine if app_used discount should be applied
    # 0.75 (25% discount) if the app was used otherwise value is 1
    app_used = 0.75 if options['app_used'].upper() == 'Y' else 1

    # returns the total cost by adding the delivery to the raw cost then multiplying by the discount values
    return (pizzas + delivery) * tuesday * app_used


# only runs the following code if the program is run directly
if __name__ == '__main__':
    print('Press ctrl+C at any point to Exit')
    # uses try catch clause to exit the program with a KeyboardInterrupt
    try:
        # runs loop_program function defined above
        loop_program()
    except KeyboardInterrupt:
        print('BPP Pizza Price Calculator Exited...')
