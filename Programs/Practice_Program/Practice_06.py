"""
Find minimum difference b/w 2 elements of array

Input:
arr1 = [5,7,10,15,20,8]

Output:
1
"""

def min_diff(arr):
    arr1 = sorted(arr)
    size = len(arr1)

    minimum = 999*999

    for i in range(size-1):
        if arr1[i+1]-arr1[i] < minimum:
            minimum = arr1[i+1] - arr1[i]

    print("Minimum differnce is", minimum)

arr = [5,7,10,15,20,8]
min_diff(arr)
