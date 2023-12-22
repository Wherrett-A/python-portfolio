""" Write and test three functions that each take two words (strings) as parameters and
return sorted lists (as defined above) representing respectively:
Letters that appear in at least one of the two words.
Letters that appear in both words.
Letters that appear in either word, but not in both"""


def letters_in_at_least_one(string1, string2):
    return sorted(list(set(list(string1) + list(string2))))


def letters_in_both(string1, string2):
    return sorted(list(set(list(string1)) & set(list(string2))))


def letters_in_either_not_both(string1, string2):
    return sorted(list(set(list(string1)) ^ set(list(string2))))


print(letters_in_at_least_one('Hello', 'World!'))
print(letters_in_both('Hello', 'World!'))
print(letters_in_either_not_both('Hello', 'World!'))
