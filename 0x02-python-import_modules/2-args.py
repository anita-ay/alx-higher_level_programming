#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    if length == 1:
        print("{} argument.".format(length - 1))
    elif length == 2:
        print("{} argument:".format(length - 1))
    else:
        print("{} arguments:".format(length - 1))

    if length > 1:
        for i in range(1, length):
            print("{}: {}".format(i, sys.argv[i]))
