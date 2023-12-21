#!/usr/bin/env python3
def loop_program():
    while True:
        run()


def run():
    greeting = 'BPP Pizza Price Calculator'

    print(greeting + '\n' + '=' * len(greeting) + '\n')

    value = take_inputs()

    # prints the total price to 2dp using :.2f format
    # unless take_inputs returned a string in which case the string is printed
    print(f'Total Price: £{value:.2f}.') if not isinstance(value, str) else print(value)


def take_inputs():
    pizzas = input('How many pizzas ordered? ')
    delivery = input('Is delivery required?(y/n) ')
    tuesday = input('Is it a Tuesday?(y/n) ')
    app_used = input('Did the customer use the app?(y/n) ')
    print('\n')

    return valid_input(pizzas=pizzas, delivery=delivery, tuesday=tuesday, app_used=app_used)


def valid_input(**options):
    # if the number of pizzas the user entered is not an integer, the function returns an error
    if not options['pizzas'].isnumeric():
        return 'Number of pizzas should be an integer.'
    if int(options['pizzas']) < 1:
        return 'Numer of pizzas should be a positive integer.'
    # iterates through delivery, tuesday, and app_used inputs to check values are either 'y' or 'n'
    # if they are not valid an error is returned
    for value in ['delivery', 'tuesday', 'app_used']:
        if options[value].upper() != 'Y' and options[value].upper() != 'N':
            return 'All inputs other than the number of pizzas should be "y" or "n".'
    return cost(options)


def cost(options):
    pizzas = 12 * int(options['pizzas'])
    delivery = 2.5 if options['delivery'].upper() == 'Y' else 0
    tuesday = 0.5 if options['tuesday'].upper() == 'Y' else 1
    app_used = 0.75 if options['app_used'].upper() == 'Y' else 1

    return (pizzas + delivery) * tuesday * app_used


# only runs the following code if the program is run directly
if __name__ == '__main__':
    print('Press ctrl+C at any point to Exit')
    try:
        loop_program()
    except KeyboardInterrupt:
        print('BPP Pizza Price Calculator Exited...')
