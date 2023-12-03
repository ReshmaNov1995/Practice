"""
Reverse words in a sentence

Input:
str = "Welcome to Python Automation"

Output:
Automation Python to Welcome
"""

def rev_word(str):
    list1 = str.split()
    rev = list1[::-1]
    print(' '.join(rev))


str = "Welcome to Python Automation"

rev_word(str)