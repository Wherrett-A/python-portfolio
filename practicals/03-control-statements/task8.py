"""Modify the "Times Table" again so that the user still enters the number of the table,
but if this number is negative the table is printed backwards. So entering "-7"
would produce the Seven Times Table starting at "12 times" down to "0 times" """

# only runs the program if the code is executed directly rather than imported
if __name__ == '__main__':

    multiplier = int(input('which times table do you require? (between 0 & 12)\n'))
    # only prints the times table if the entered number is in range
    if -12 <= multiplier <= 12:

        # iterates through numbers 0-12
        for num in range(13):
            # 'is_positive' = 0 when multiplier is negative and 1 when multiplier is positive
            is_positive = (multiplier / abs(multiplier) + 1) / 2
            # uses value of 'is_positive' to determine whether numbers increment or decrement
            mult = (12 - num) * abs(is_positive - 1) + num * is_positive

            # prints the multiple for each numer in the loop
            print(f'{mult} × {abs(multiplier)} = {mult * abs(multiplier)}')
    else:
        # prints error if number is not in correct range
        print('number should be between 0 & 12')
