"""Write and test a function that determines if a given integer is a prime number. A
prime number is an integer greater than 1 that cannot be produced by multiplying
two other integers."""


def get_factors(integer):
    if type(integer) is not int:
        raise ValueError("get_factors function must be passed a positive integer")
    if integer < 1:
        raise ValueError("get_factors function must be passed a positive integer")

    return [i for i in range(1,  integer+1) if not integer % i]


def is_prime(integer):
    return len(get_factors(integer)) == 2


try:
    print(is_prime(50))  # not prime
    print(is_prime(1))  # not prime
    print(is_prime(23))  # prime
except ValueError as error:
    print(error)
