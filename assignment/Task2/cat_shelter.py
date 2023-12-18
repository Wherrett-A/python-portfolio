#!/usr/bin/env python3
# import sys to allow the use of console arguments
import sys


def open_file(file_path):
    # uses with when opening the file as with is self-closing
    # file is opened as read-only and the data is stored in variable log
    with open(file_path, 'r') as log:
        # the file path is printed to console to the user can see which file has been analysed
        print('file_path')
        # analyse_ file() function then analyses the file
        # when passing the file data to the function .read() is used to only send the file contents
        # and .split('\n') is used to convert the contents into a list split by new lines
        analyse_file(log.read().split('\n'))


def analyse_file(log):
    # initial variables are set
    # ours will contain the number of visits from the users cat
    ours = 0
    # theirs will contain the number of visits from other cats
    theirs = 0
    # visit_lengths will store the length of each visit from the users cat as an array
    visit_lengths = []

    # each line of the file is then iterated through (each visit in the 'log' list)
    # [:-1] is used to ignore the last item in the list which will always be 'END'
    for visit in log[:-1]:
        # each visit is then split by commas making a list so that it is easier to access each value
        visit_list = visit.split(',')
        # if the cat belongs to the user 'our' value increments by 1
        # and the length of the visit (departure time - arrival time) is appended to the 'visit_length' array
        if visit_list[0] == 'OURS':
            ours += 1
            visit_lengths.append(int(visit_list[2])-int(visit_list[1]))

        # if it is another cat the 'theirs' variable is incremented by 1
        theirs += 1 if visit_list[0] == 'THEIRS' else 0

    # total time is calculated by adding all values in the 'visit_lengths' array
    # and passing the total to time function to format the time to hours and minutes
    total_time = time(sum(visit_lengths))
    # average is calculated by dividing the sum by the length of the ' visit_length' array
    # this is also formatted by the time function
    average = time(round((sum(visit_lengths)/len(visit_lengths))))
    # longest takes the maximum time from the array and passes it to the time function
    longest = time(max(visit_lengths))
    # shortest takes the minimum time from the array and passes it to the time function
    shortest = time(min(visit_lengths))

    # all values are then passed to the output function which prints them
    output(ours, theirs, total_time, average, longest, shortest)


def time(total):
    # if the total time is over an hour, the time is returned in both hours and minutes
    # otherwise only minutes are returned
    # value returned is a string following the format 'A Hours, B Minutes' or just 'B Minutes'
    return f'{total // 60} Hours, {total % 60} Minutes' if total // 60 else f'{total % 60} Minutes'


def output(ours, theirs, total_time, average, longest, shortest):
    # define the greeting
    greeting = 'Log File Analysis'

    # print the greeting along with a line of '='s of same character length forming an underline
    print(greeting + '\n' + '=' * len(greeting) + '\n')
    # prints the values using triple quotes to form a multiline string
    print(f'''Cat Visits: {ours}
Other Cats: {theirs}

Total Time in House: {total_time}

Average Visit Length: {average}
Longest Visit: {longest}
Shortest Visit: {shortest}''')


# stores arguments from the console in as a list
# using [1:] to remove the first argument which would be the name of the python file
args = sys.argv[1:]

# if the list of arguments is empty prints an error to the console
if not args:
    print('Missing command line argument!')

# iterates through each argument given and try's to look for a file with the same path
for file in args:
    try:
        open_file(file)
    # if the file is not found an error will be printed to the console
    except FileNotFoundError:
        print(f'cannot open file "{file}"')
