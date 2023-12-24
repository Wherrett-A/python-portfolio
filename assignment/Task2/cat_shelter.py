#!/usr/bin/env python3
# import sys to allow the use of console arguments
import sys


def open_file(file_path):
    # uses with when opening the file as with is self-closing
    with open(file_path, 'r') as log:
        # the file path is printed to console to the user can see which file has been analysed
        print('file_path')
        analyse_file(log.read().split('\n'))


def analyse_file(log):
    ours = 0
    theirs = 0
    visit_lengths = []

    # [:-1] is used to ignore the last item in the list which will always be 'END'
    for visit in log[:-1]:
        visit_list = visit.split(',')
        if visit_list[0] == 'OURS':
            ours += 1
            visit_lengths.append(int(visit_list[2])-int(visit_list[1]))

        theirs += 1 if visit_list[0] == 'THEIRS' else 0

    total_time = time(sum(visit_lengths))
    average = time(round((sum(visit_lengths)/len(visit_lengths))))
    longest = time(max(visit_lengths))
    shortest = time(min(visit_lengths))

    output(ours, theirs, total_time, average, longest, shortest)


def time(total):
    # if the total time is over an hour, the time is returned in both hours and minutes
    # otherwise only minutes are returned
    # value returned is a string following the format 'A Hours, B Minutes' or just 'B Minutes'
    return f'{total // 60} Hours, {total % 60} Minutes' if total // 60 else f'{total % 60} Minutes'


def output(ours, theirs, total_time, average, longest, shortest):
    greeting = 'Log File Analysis'

    print(greeting + '\n' + '=' * len(greeting) + '\n')
    print(f'Cat Visits: {ours}\n'
          f'Other Cats: {theirs}\n\n'
          f'Total Time in House: {total_time}\n\n'
          f'Average Visit Length: {average}\n'
          f'Longest Visit: {longest}\n'
          f'Shortest Visit: {shortest}')


# using [1:] to remove the first argument which would be the name of the python file
args = sys.argv[1:]

# if the list of arguments is empty prints an error to the console
if not args:
    print('Missing command line argument!')

for file in args:
    try:
        open_file(file)
    except FileNotFoundError:
        print(f'cannot open file "{file}"')
