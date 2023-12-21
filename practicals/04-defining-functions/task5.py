"""Write and test a function that converts a temperature measured in degrees
centigrade into the equivalent in fahrenheit, and another that does the reverse
conversion. Test both functions. (Google will find you the formulae)."""


def ctof(temp):
    """converts Centigrade to Fahrenheit"""
    return int(temp) * 1.8 + 32


def ftoc(temp):
    """converts Fahrenheit to Centigrade"""
    return (int(temp) - 32) / 1.8


if __name__ == '__main__':
    # coverts 40°C to °F, should be 104
    print(ctof(40))
    # coverts 104°F to °C, should be 40
    print(ftoc(104))
