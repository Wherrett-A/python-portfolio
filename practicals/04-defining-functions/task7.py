"""Modify the previous program so that it can process any number of values. The input
terminates when the user just pressed "Enter" at the prompt rather than entering a
value."""


def ftoc(temp):
    """converts Fahrenheit to Centigrade"""
    return (int(temp) - 32) / 1.8


if __name__ == '__main__':
    temperatures = {}

    print('use F or C at end of temperature to define whether it is in fahrenheit or celsius')
    num_of_inputs = int(input('how many temperatures would you like to input: '))
    for i in range(1, num_of_inputs+1):
        user_temp = input(f'Enter temperature {i}: ')
        if user_temp[-1].upper() == 'F':
            temperatures.setdefault(ftoc(user_temp[:-1]), user_temp)
        elif user_temp[-1].upper() == 'C':
            temperatures.setdefault(int(user_temp[:-1]), user_temp)

    centigrade = temperatures.keys()
    max_temp = temperatures[max(centigrade)]
    min_temp = temperatures[min(centigrade)]
    avg_temp = str(sum(centigrade)/len(centigrade)) + 'C'

    print(f"""maximum is {max_temp}
minimum is {min_temp}
mean temperature is {avg_temp}""")
