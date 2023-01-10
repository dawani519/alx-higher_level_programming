#!/usr/bin/python3
for character in range(97, 123):
    if 101 != character and 113 != character:
        print("{}".format(chr(character)), end="")
