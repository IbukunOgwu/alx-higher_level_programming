#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = sys.argv
    length = len(arg) - 1
    if length == 0:
        print("{} arguments.".format(0))
    elif length == 1:
        print("{} argument:".format(length))
        print("{}: {}".format(length, arg[1]))
    else:
        print("{} arguments:".format(length))
        for i in range(length):
            print("{}: {}".format(i + 1, arg[i + 1]))
