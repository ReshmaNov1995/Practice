"""
PostFix Expression

Input:
list1 = [2,3,*,6,-]

Output:
0

# Algorithm
# 1. Evaluate each character in postfix expression
# 2. If Operand is encountered, push into stack
# 3. If Operator is encountered, pop two characters from stack which were already filled in stack
#       first = top element from stack
#       second = second element from stack
# 4. Check for operator & push into stack after operation.
#       second operator first
# 5. return top element from stack
"""

def eval_Expression(arr):
    stack = [] # Empty Stack
    operator = ["+", "*", "-", "/", "%"]

    for item in arr: # Evaluate each character in postfix expression
        if item not in operator: # Operand
            stack.append(item) # push into stack

        else: # Operator
            first = int(stack.pop())
            second = int(stack.pop())

            if (item == "+"):
                stack.append(second + first)

            if (item == "-"):
                stack.append(second - first)

            if (item == "*"):
                stack.append(second * first)

            if (item == "/"):
                stack.append(second / first)

            if (item == "%"):
                stack.append(second % first)

    return stack[-1] # Last value of the stack

arr = ["2", "1", "+", "3", "*"]
print(eval_Expression(arr))
