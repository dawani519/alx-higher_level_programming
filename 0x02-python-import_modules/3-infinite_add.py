#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    if len(args) == 0:
        print("No arguments given")
    else:
        result = 0
        for arg in args:
            result += int(arg)
            print(result)
