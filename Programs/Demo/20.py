"""
Reverse a list

Input:
list5 = [3,4,7,9,10]

Output:
[10, 9, 7, 4, 3]
"""

def rev_list(list5):
    size = len(list5)
    list6 = []

    for i in range(size-1, -1, -1):
        list6.append(list5[i])
    print(list6)


list5 = [3,4,7,9,10]
rev_list(list5)