#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    arg = sys.argv

    if len(arg) == 1:
        print("0 arguments.")
    elif len(arg) == 2:
        arg.pop(0)
        print("{} argument:".format(len(arg)))

        for i, cont in enumerate(arg):
            print("{} : {}".format(i + 1, cont))
    else:
        arg.pop(0)
        print("{} arguments:".format(len(arg)))

        for i, cont in enumerate(arg):
            print("{} : {}".format(i + 1, cont))
