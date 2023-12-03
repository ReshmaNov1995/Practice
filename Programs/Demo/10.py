"""
Remove duplicate from sorted array

Input:
arr = [10,20,30,30,40,50]

Output:
[10,20,30,40,50]
"""

def remove_dup(arr):
    size = len(arr)
    list1 = []

    for i in range(size-1):
        if arr[i] != arr[i+1]:
            list1.append(arr[i])
    list1.append(arr[-1])

    print(list1)

arr = [10, 20, 30, 30, 40, 50]

remove_dup(arr)