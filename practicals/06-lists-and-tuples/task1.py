"""Write a function that accepts a positive integer as a parameter and then returns a
representation of that number in binary (base 2)."""


def int_to_bin(integer):
    if type(integer) is not int:
        raise ValueError("int_to_bin function must be passed a positive integer")
    if integer < 1:
        raise ValueError("int_to_bin function must be passed a positive integer")
    binary = []
    while integer != 0:
        binary.append(str(integer % 2))
        integer //= 2
    return ''.join(binary)


try:
    print(int_to_bin(5))
except ValueError as error:
    print(error)
