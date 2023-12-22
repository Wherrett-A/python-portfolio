""" Write and test a function that does such encryption. It should
randomly generate an interval (between 2 and 20), space the message out
accordingly, and should fill the gaps with random letters. The function should
return the encrypted message and the interval used."""

import random


def obfuscate(message):
    interval = random.randint(2, 20)
    # list of all lowercase and uppercase characters
    characters = [chr(n) for n in
                  list(range(ord('a'), ord('z') + 1)) +
                  list(range(ord('A'), ord('Z') + 1))]

    new_length = len(message) + len(message) // (interval-1)

    message_list = list(message)
    for index in range(interval, new_length, interval):
        message_list.insert(index, random.choice(characters))

    return ''.join(message_list), interval


def deobfuscate(message, interval):
    deobfuscated = [message[0]]
    for i in range(len(message)):
        if i % interval:
            deobfuscated.append(message[i])
    return ''.join(deobfuscated)


obfuscated_string, key = obfuscate('The Quick Brown Fox Jumped Over The Lazy Dog.')
print(obfuscated_string)

deobfuscated_string = deobfuscate(obfuscated_string, key)
print(deobfuscated_string)
