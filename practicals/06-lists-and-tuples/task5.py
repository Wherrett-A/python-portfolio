""" Write and test a function that does such encryption. It should
randomly generate an interval (between 2 and 20), space the message out
accordingly, and should fill the gaps with random letters. The function should
return the encrypted message and the interval used."""

import random


def obfuscate(message):
    interval = random.randint(2, 20)
    characters = [chr(n) for n in
                  list(range(ord('a'), ord('z')+1)) +
                  list(range(ord('A'), ord('Z')+1))]

    message_list = list(message)
    for index in range(interval, len(message), interval):
        message_list.insert(index, random.choice(characters))

    return ''.join(message_list), interval


obfuscated_string, key = obfuscate('The Quick Brown Fox Jumped Over The Lazy Dog.')
print(obfuscated_string)
print(key)
