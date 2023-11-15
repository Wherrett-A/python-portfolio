"""Write a program that prompts a user to enter a temperature in Celsius, and then
displays the corresponding temperature in Fahrenheit"""

# only runs the program if the code is executed directly rather than imported
if __name__ == '__main__':
    # prompts user to enter a temperature in Celsius then stores in 'celsius' variable as a float
    celsius = float(input('Enter a temperature in Celsius: '))
    # converts celsius temperature to fahrenheit
    fahrenheit = (celsius * 1.8) + 32

    # uses inbuilt print function to print the Celsius and Fahrenheit temperature
    print(f'{celsius}℃ is {fahrenheit}℉')
