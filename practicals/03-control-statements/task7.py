"""Modify your "Times Table" program so that the user enters the number of the table
they require. This number should be between 0 and 12 inclusive."""

# only runs the program if the code is executed directly rather than imported
if __name__ == '__main__':

    multiplier = int(input('which times table do you require? (between 0 & 12)\n'))
    # only prints the times table if the entered number is in range
    if 0 < multiplier <= 12:
        # iterates through numbers 0-12
        for num in range(13):
            # prints the multiple for each numer in the loop
            print(f'{num} × {multiplier} = {num * multiplier}')
    else:
        # prints error if number is not in correct range
        print('number should be between 0 & 12')
