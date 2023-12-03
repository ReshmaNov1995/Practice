"""
Find minimum difference b/w 2 elements of array

Input:
arr1 = [5,7,10,15,20,8]

Output:
1
"""

def min_diff(arr1):
    arr2 = sorted(arr1)
    size = len(arr1)
    min = 999*999

    for i in range(size-1):
        if arr2[i+1]-arr2[i] < min:
            min = arr2[i+1]-arr2[i]
    print(min)

arr1 = [5,10,15,20,8]
min_diff(arr1)