"""
Finding duplicate Characters in a string

Input:
str = "Reshmas"

Output:
s
"""

def dup_char():
    str = input()

    list = []

    for i in str:
        list.append(i)
    print(list)

    dict = {}
    for i in range(len(list)):
        if list[i] not in dict:
            dict[list[i]] = 1

        else:
            dict[list[i]] = dict[list[i]]+1

    for index,value in enumerate(set(list)): # It will seperate the index & value
        if dict[list[index]] > 1:

            print("The duplicate key is", list[index], dict[list[index]])

dup_char()