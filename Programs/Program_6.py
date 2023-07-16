# Find minimum difference b/w 2 elements of array

# Algorithm
# Sort the elements of array
# Initialise the first difference value to be largest. Start comparing the difference of first element with it
# Compare element with its adjacent element & keep tracking of minimum element

def minimum_diff_element(arr1):
    arr = sorted(arr1) # Sort in ascending order
    print(arr)
    size = len(arr)
    min_diff = 9999*999

    for i in range(size-1):
        if (arr[i+1] - arr[i] < min_diff):
            min_diff = arr[i+1] - arr[i]
    return min_diff

arr = [5,32,45,4,12,18,25]
print("Minimum difference b/w 2 elements of array", minimum_diff_element(arr))