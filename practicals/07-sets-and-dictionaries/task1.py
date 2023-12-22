"""Write and test a function that takes a string as a parameter and returns a sorted list
of all the unique letters used in the string. So, if the string is cheese, the list
returned should be ['c', 'e', 'h', 's']."""


def unique_characters(string):
    return sorted(list(set(list(string))))


# capital letters come alphabetically before lower case
print(unique_characters('Hello World!'))
print(unique_characters('cheese'))
