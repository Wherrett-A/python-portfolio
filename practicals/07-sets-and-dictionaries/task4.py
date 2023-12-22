"""Write a program that processes a string representing a message and reports the six
most common letters, along with the number of times they appear. Case should
not matter, so "E" and "e" are considered the same."""


def analyse(message):
    characters = {}
    for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        characters.setdefault(char, message.upper().count(char))
    return sorted(characters.items(), key=lambda value: value[1], reverse=True)


if __name__ == '__main__':
    string = input('Type a string: ')
    print(analyse(string)[:6])

