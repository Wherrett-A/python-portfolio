"""Write a program that takes a centigrade temperature and displays the equivalent in
fahrenheit. The input should be a number followed by a letter C. The output should
be in the same format."""


def convert_temp(temp):
    """uses last character (c/f) to define if temperature is in Celsius or Fahrenheit respectively"""
    # use [-1] to get the last character
    if temp[-1].upper() == 'C':
        return int(temp[:-1]) * 1.8 + 32
    elif temp[-1].upper() == 'F':
        return (int(temp[:-1]) - 32) * 1.8


if __name__ == '__main__':
    print('use F or C at end of temperature to define whether it is in fahrenheit or celsius')
    user_temp = input('type a temperature to covert: ')
    print(convert_temp(user_temp))
