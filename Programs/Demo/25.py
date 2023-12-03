"""
Finding duplicate Characters in a string

Input:
str = "Reshmas"

Output:
s
"""

def dup_char(str):
    size = len(str)

    dict = {}

    for i in range(size):
        if str[i] not in dict:
            dict[str[i]] = 1
        else:
            dict[str[i]] = dict[str[i]] + 1

        if dict[str[i]] > 1:
            print(str[i], dict[str[i]])

str = "reshmas"
dup_char(str)