"""In a long career for Yorkshire, Geoffrey Boycott played 609 matches, batted 1014
times, was not out 162 times, and scored 48426 runs. Write a program to calculate
and display Boycott's batting average."""

# only runs the program if the code is executed directly rather than imported
if __name__ == '__main__':
    # defines variables needed for batting average calculation
    batted = 1014
    not_out = 162
    runs_scored = 48426

    # calculates the average and sores in 'average' variable
    average = runs_scored / (batted - not_out)

    # prints the batting average to the console
    print('your batting average is', average)
