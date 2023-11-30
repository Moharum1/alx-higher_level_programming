#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    arg = sys.argv

    if arg == 1:
        print("0")
    else:
        arg.pop(0)
        count = 0

        for number in arg:
            count += int(number)
        print(count)
