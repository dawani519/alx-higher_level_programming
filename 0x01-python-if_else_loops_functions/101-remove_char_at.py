#!/usr/bin/python3
def remove_char_at(str, n):
    for letter in range(97, 123):
        if chr(letter) != 'q' and chr(letter) != 'e':
            print("{}".format(chr(letter)), end="")
