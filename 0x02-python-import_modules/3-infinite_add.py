#!/usr/bin/python3
def add_args():
    import sys
    total = 0
    for arg in sys.argv[1:]:
        total += int(arg)
        print(total)
        if __name__ == "__main__":
            add_args()
