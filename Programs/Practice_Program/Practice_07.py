"""
Find maximum difference b/w 2 elements of array

Input:
arr1 = [5,7,10,15,20,8]

Output:
5
"""

def max_diff(arr):
    arr1 = sorted(arr)

    size = len(arr1)

    max = -999*999

    for i in range(size-1):
        if arr1[i+1] - arr1[i] > max:
            max = arr1[i+1] - arr1[i]
    print("Maximum difference is", max)

arr = [5,7,10,15,20,8]
max_diff(arr)