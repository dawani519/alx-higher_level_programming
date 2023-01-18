#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argument = sys.argv[1:]
    total = 0
    for arg in argument:
        total += int(arg)
        print(total)
