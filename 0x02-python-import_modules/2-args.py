#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    i = 1
    for i in len(argv):
        print("{}: {}".format(i, len(argv)))
