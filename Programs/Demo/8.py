"""
PostFix Expression

Input:
list1 = [2,3,*,6,-]

Output:
0
"""

def eval_Expression(arr):
    stack = [] # Empty Stack
    operator = ["+", "*", "-", "/", "%"]

    for i in arr: # Evaluate each character in postfix expression
        if i not in operator: # Operand
            stack.append(i) # push into stack

        else: # Operator
            first = int(stack.pop())
            second = int(stack.pop())

            if (i == "+"):
                stack.append(second + first)

            if (i == "-"):
                stack.append(second - first)

            if (i == "*"):
                stack.append(second * first)

            if (i == "/"):
                stack.append(second / first)

            if (i == "%"):
                stack.append(second % first)

    return stack[-1] # Last value of the stack

arr = ["2", "1", "+", "3", "*"]
print(eval_Expression(arr))
