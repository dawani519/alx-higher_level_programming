#!/usr/bin/python3
def uppercase(str):
    str = "best school 98 battery street"
    for str in range(65, 90):
        if ord(str) >= 65 and ord(str) <= 90:
            print("{}".format(str))
        else:
            print("{}".format(str), end="")
