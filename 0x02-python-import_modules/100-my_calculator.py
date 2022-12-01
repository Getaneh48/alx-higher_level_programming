#!/usr/bin/python3

if __name__ == "__main__":

    from calculator_1 import add, sub, mul, div
    import sys

    opr = ['+', '-', '*', '/']
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>", end="\n")
        sys.exit(1)

    if sys.argv[2] not in opr:
        print("Unknown operator. Available \
operators: +, -, * and /", end="\n")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    op = sys.argv[2]
    result = 0

    if op == '+':
        result = add(a, b)
    elif op == '-':
        result = sub(a, b)
    elif op == '*':
        result = mul(a, b)
    else:
        result = div(a, b)

    print("{} {} {} = {}".format(a, op, b, result), end="\n")
