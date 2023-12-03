"""
Minimum Element from the array
Maximum Element from the array

Input:
A = [63, 54, 98, 34, 89, 42, 18]

Output:
98
"""

def min_element(arr):
    size = len(arr)
    min = arr[0]

    for i in range(size):
        if arr[i] < min:
            min = arr[i]

    print(min)

A = [63, 54, 98, 34, 89, 42, 18]
min_element(A)

def max_element(arr):
    size = len(arr)
    max = arr[-1]

    for i in range(size):
        if arr[i] > max:
            max = arr[i]

    print(max)

A = [63, 54, 98, 34, 89, 42, 18]
max_element(A)