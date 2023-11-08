'''Over the summer, temperatures in Yorkshire reached 38.4C. Write a program that
converts this value in Celsius to the equivalent temperature in Fahrenheit, and then
displays both.'''

if __name__ == '__main__':
    celsius = 38.4
    fahrenheit = (celsius * 1.8) + 32

    print(f'{celsius}℃ is {fahrenheit}℉')
