"""
Length of Last word

Input:
String = "Welcome to Python Automation"

Output:
10
"""

def last_word(str):
    str1 = str.split()

    if str1 == 1:
        return len(str1)

    else:
        return len(str1[-1])

str = "Welcome to Python Automation"
print(last_word(str))