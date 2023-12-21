"""Functions are often used to validate input. Write a function that accepts a single
integer as a parameter and returns True if the integer is in the range 0 to 100
(inclusive), or False otherwise. Write a short program to test the function."""


def valid_range(num):
    """checks if integer is in range 0-100 inclusive"""
    return 0 <= int(num) <= 100


if __name__ == '__main__':
    usr_num = input('input a number to check if it is in the range: ')
    print(valid_range(usr_num))
