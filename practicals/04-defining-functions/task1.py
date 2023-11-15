"""Functions are often used to validate input. Write a function that accepts a single
integer as a parameter and returns True if the integer is in the range 0 to 100
(inclusive), or False otherwise. Write a short program to test the function."""


# valid_range function returns true if number is in desired range and false if it is not in range
def valid_range(num):
    """checks if integer is in range 0-100 inclusive"""
    return 0 <= int(num) <= 100


# only runs the program if the code is executed directly rather than imported
if __name__ == '__main__':
    # takes a number as user input to be checked with the 'valid_range' function
    usr_num = input('input a number to check if it is in the range: ')
    # passes the user entered number to the function the prints the result
    print(valid_range(usr_num))
