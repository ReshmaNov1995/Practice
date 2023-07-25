# Find maximum difference b/w 2 elements of array

# Algorithm
# Sort the elements of array
# Initialise the first difference value to be smallest.
# Compare element with its adjacent element & keep tracking of maximum difference

def max_diff_element(arr):
    arr1 = sorted(arr)
    size = len(arr1)
    diff = - 9999*999

    for i in range(size-1):
        if (arr1[i+1]-arr1[i] > diff): # arr[1]-arr[0] > -9989001. 5-4 > -9989001.
            diff = arr1[i+1]-arr1[i] # reassign the value of diff.
    return diff

arr = [5, 32, 45, 4, 12, 18, 25]
print("Maximum difference b/w 2 elements of array", max_diff_element(arr))