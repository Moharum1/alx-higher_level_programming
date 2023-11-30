#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul
    import sys
    arg = sys.argv

    if len(arg) < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        if arg[2] not in ["+", "-", "*", "/"]:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        else:
            a = int(arg[1])
            opr = arg[2]
            b = int(arg[3])

            if opr == "+":
                print("{} {} {} = {}".format(a, opr, b, add(a, b)))
            elif opr == "-":
                print("{} {} {} = {}".format(a, opr, b, sub(a, b)))
            elif opr == "*":
                print("{} {} {} = {}".format(a, opr, b, mul(a, b)))
            else:
                print("{} {} {} = {}".format(a, opr, b, div(a, b)))
