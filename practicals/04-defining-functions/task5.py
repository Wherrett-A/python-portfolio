"""Write and test a function that converts a temperature measured in degrees
centigrade into the equivalent in fahrenheit, and another that does the reverse
conversion. Test both functions. (Google will find you the formulae)."""


# defines convert_temperature function
def convert_temp(temp):
    """uses last character (c/f) to define if temperature is in Celsius or Fahrenheit respectively"""
    if temp[-1:].upper() == 'C':
        return int(temp[:-1]) * 1.8 + 32
    elif temp[-1:].upper() == 'F':
        return (int(temp[:-1]) - 32) * 1.8
    else:
        return


# only runs the program if the code is executed directly rather than imported
if __name__ == '__main__':
    print('use F or C at end of temperature to define whether it is in fahrenheit or celsius')
    # takes a string from the user to pass to process function
    user_temp = input('type a temperature to covert: ')
    # prints returned string from the processed function after the users string has been entered
    print(process(user_string))
