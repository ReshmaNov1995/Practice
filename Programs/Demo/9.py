"""
Length of Last word

Input:
String = "Welcome to Python Automation"

Output:
10
"""

def len_latsword(str):
    str1 = str.split()
    print(str1)

    if str1 == 1:
        print(len(str1))

    else:
        print(len(str1[-1]))



String = "Welcome"

len_latsword(String)