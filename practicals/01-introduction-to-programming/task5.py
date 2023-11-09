'''The Head of Computing at the University of Poppleton is tasked with dividing a
group of students into lab groups. A lab group is 24 students, since this is the
number of PCs in a lab. Write a program that calculates how many groups are
needed for the following number of students: 113, 175, 12. Display how many full
groups there will be, and how many students will be in the smaller "left over"
group.'''

# only runs the program if the code is executed directly rather than imported
if __name__ == '__main__':
    # variable containing the desired group size
    size = 24
    # array of number of students per class to be split into groups
    students = [113, 175, 12]

    # iterates through classes and stores the number of students in variable 'val'
    for val in students:
        # uses floor division to find the number of whole groups and modulus to find the numer of students left over
        groups = val // size
        remainder = val % size

        # prints the number of groups and the number of left over students to the console
        print(f'The class of {val} students would have {groups} groups with {remainder} students left over.')
