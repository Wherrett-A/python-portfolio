'''The Head of Computing at the University of Poppleton is tasked with dividing a
group of students into lab groups. A lab group is usually 24 students, but this is
sometimes varied to create groups of similar size. Write a program that prompts for
the number of students and group size, and then displays how many groups will be
needed and how many will be left over in a smaller group.'''

# only runs the program if the code is executed directly rather than imported
if __name__ == '__main__':
    # inputs get the desired group size and the number of students
    size = int(input('what is the desired group size? '))
    students = int(input('How many student need to be split into groups? '))

    # uses floor division to find the number of whole groups and modulus to find the numer of students left over
    groups = students // size
    remainder = students % size

    # prints the number of groups and the number of left over students to the console
    print(f'The class of {students} students would have {groups} groups with {remainder} students left over.')
