#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    if len(argv) == 0:
        print("Number of argument(s): 0.")
    elif len(argv) == 1:
        print("Number of argument: 1.")
        print(f"1: {argv[0]}")
    else:
        print(f"Number of arguments: {len(argv)}")
        for index, arg in enumerate(argv):
            print(f"{index+1}: {arg}")
