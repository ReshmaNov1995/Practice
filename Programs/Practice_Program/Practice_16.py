"""
First Non Repeating character in a string with its index position

Input:
str_r = "NETSETOSNETM"

Output:
O:6
"""

def non_repeating_character(str):
    size = len(str)

    dict = {}

    for i in range(size):
        if str[i] not in dict:
            dict[str[i]] = 1

        else:
            dict[str[i]] = dict[str[i]] + 1

    # print(dict)


    count = 0

    for i in range(size):
        if dict[str[i]] == 1:
            print(str[i], count)

        count += 1

str = "NETSETOSNETM"
non_repeating_character(str)


