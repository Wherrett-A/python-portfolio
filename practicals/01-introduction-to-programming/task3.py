'''Over the summer, temperatures in Yorkshire reached 38.4C. Write a program that
converts this value in Celsius to the equivalent temperature in Fahrenheit, and then
displays both.'''

# only runs the program if the code is executed directly rather than imported
if __name__ == '__main__':
    celsius = 38.4
    # converts celsius temperature to fahrenheit
    fahrenheit = (celsius * 1.8) + 32

    # uses inbuilt print function to print the Celsius and Fahrenheit temperature
    print(f'{celsius}℃ is {fahrenheit}℉')
