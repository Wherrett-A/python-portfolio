"""Write a program that manages a list of countries and their capital cities. It should
prompt the user to enter the name of a country. If the program already "knows"
the name of the capital city, it should display it. Otherwise it should ask the user to
enter it. This should carry on until the user terminates the program (how this
happens is up to you)."""
# Current Countries are United Kingdom, India, Greece
import pickle


def get_dictionary():
    try:
        with open('dictionary.task3', 'rb') as dictionary:
            return pickle.load(dictionary)
    except FileNotFoundError:
        open('dictionary.task3', 'x')
        return {}
    except EOFError:
        return {}


def run():
    country_input = input('Enter a country: ').upper()
    try:
        print(f'Capital city: {capital_cities[country_input].title()}')
    except KeyError:
        print('We do not have a Capital City listed for this Country, please enter it below')
        capital_cities.setdefault(country_input, input('Capital City: ').upper())
    return capital_cities


capital_cities = get_dictionary()

try:
    print('press "ctrl+c" at any point to quit')
    while True:
        capital_cities = run()
except KeyboardInterrupt:
    with open('dictionary.task3', 'wb') as dictionary:
        pickle.dump(capital_cities, dictionary)
