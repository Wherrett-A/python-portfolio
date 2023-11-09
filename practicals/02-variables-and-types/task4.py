'''A kindly teacher wishes to distribute a tub of sweets between her pupils. She will
first count the sweets and then divide them according to how many pupils attend
that day. Write a program that will tell the teacher how many sweets to give to each
pupil, and how many she will have left over'''

# only runs the program if the code is executed directly rather than imported
if __name__ == '__main__':
    # inputs get the number of sweets and number of students
    sweets = int(input('How many sweets are in the tub? '))
    students = int(input('How many student are there? '))

    # uses floor division to find the number of sweets per student and modulus to find the numer of sweets left over
    num = sweets // students
    remainder = sweets % students

    # prints the number of groups and the number of left over students to the console
    print(f'Each student should get {num} sweets and you will have {remainder} sweets left over.')
