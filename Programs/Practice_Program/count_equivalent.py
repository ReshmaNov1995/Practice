"""
pattern = "{}[](){}"
handled
not handled
"""


def pattern(arg):

    curlycount = 0
    curlycount1 = 0
    squarecount = 0
    squarecount1 = 0
    count = 0
    count1 = 0
    for i in arg:
        if i == '{':
            curlycount = curlycount + 1

        if i == '}':
            curlycount1 = curlycount1 + 1

        if i == '[':
            squarecount = squarecount + 1

        if i == ']':
            squarecount1 = squarecount1 + 1

        if i == '(':
            count = count + 1

        if i == ')':
            count1 = count1 + 1

    if curlycount == curlycount1:
        print("Handled")
    else:
        print("Not Handled")

    if squarecount == squarecount1:
        print("Handled")
    else:
        print("Not Handled")

    if count == count1:
        print("Handled")
    else:
        print("Not Handled")

    print(curlycount, squarecount, count)


arg = "{[(){}]}{}"
pattern(arg)