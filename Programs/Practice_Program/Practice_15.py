"""
Reverse words in a sentence

Input:
str = "Welcome to Python Automation"

Output:
Automation Python to Welcome
"""

def reverse_sentence(str):
    list1 = str.split()
    rev = list1[::-1]
    print(rev)
    print(" ".join(rev))



str = "Welcome to Python Automation"
reverse_sentence(str)