"""
Reverse a list

Input:
list5 = [3,4,7,9,10]

Output:
[10, 9, 7, 4, 3]
"""

def reverse_list(list1):
    size = len(list1)
    list2 = []
    for i in range(size-1,-1,-1): # arg as 4,-1; 3,-1; 2,-1; 1,-1; 0,-1. Atlast -1 is mandatory to get a reverse order.
        list2.append(list1[i])
    print(list2)


list1 = [3,4,7,9,10]
reverse_list(list1)

