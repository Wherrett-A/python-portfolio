"""Last week you wrote a program that processed a collection of temperature readings
entered by the user and displayed the maximum, minimum, and mean. Create a
version of that program that takes the values from the command-line instead. Be
sure to handle the case where no arguments are provided!"""
import sys


def ftoc(temp):
    """converts Fahrenheit to Centigrade"""
    return (int(temp) - 32) / 1.8


def run(temps):
    temperatures = {}

    for temp in temps:
        if temp[-1].upper() == 'F':
            temperatures.setdefault(ftoc(temp[:-1]), temp)
        elif temp[-1].upper() == 'C':
            temperatures.setdefault(int(temp[:-1]), temp)
        else:
            print('temperature must end with C or F')
            break

    if temperatures:
        centigrade = temperatures.keys()
        max_temp = temperatures[max(centigrade)]
        min_temp = temperatures[min(centigrade)]
        avg_temp = str(sum(centigrade)/len(centigrade)) + 'C'

        print(f"""maximum is {max_temp}
minimum is {min_temp}
mean temperature is {avg_temp}""")


arguments = sys.argv
arguments.pop(0)
if not arguments:
    print('this program uses command line arguments\n'
          'arguments should be separated by a space and be a number followed by F or C\n'
          'meaning the temperature is Fahrenheit or Centigrade respectively')
else:
    run(arguments)
