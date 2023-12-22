"""Write and test a function that takes an integer as its parameter and returns the
factors of that integer. (A factor is an integer which can be multiplied by another to
yield the original)."""


def get_factors(integer):
    if type(integer) is not int:
        raise ValueError("get_factors function must be passed a positive integer")
    if integer < 1:
        raise ValueError("get_factors function must be passed a positive integer")

    return [i for i in range(1,  integer+1) if not integer % i]


try:
    print(get_factors(50))
except ValueError as error:
    print(error)
