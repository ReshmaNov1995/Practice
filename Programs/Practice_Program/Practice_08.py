"""
PostFix Expression

Input:
list1 = [2,3,*,6,-]

Output:
0
"""

def postfix(list):
    stack = []
    operator = ["+", "*", "-", "/", "%"]

    for i in range(len(list)):
        if list[i] not in operator: #operand
            stack.append(list[i])

        else:
            first = int(stack.pop())
            second = int(stack.pop())

            if list[i] == "+":
                stack.append(second + first)

            if list[i] == "-":
                stack.append(second - first)

            if list[i] == "*":
                stack.append(second * first)

            if list[i] == "/":
                stack.append(second / first)

            if list[i] == "%":
                stack.append(second % first)

    print(stack[-1])

list1 = ["2","3","*","6","-"]
postfix(list1)