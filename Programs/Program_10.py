# Remove duplicate from sorted array

# Algorithm 2
# pivot = 0
# for last_o in range(0, n-1):
#     if arr[last_o] != arr[last_o+1]:
#         arr[pivot] = arr[last_o]
#         pivot += 1
# arr[pivot] = arr[n-1]

# Method - 1:
def remove_duplicates_space(arr):
    n = len(arr)

    if n == 0 or n ==1:
        return arr

    temp = [0]*n # temporary variable size
    pivot = 0

    for last_o in range(0, n-1): # second last element
        if arr[last_o] != arr[last_o + 1]:
            temp[pivot] = arr[last_o]
            pivot = pivot+1
    temp[pivot] = arr[n - 1] # To write the last value inside.
    return temp[0:pivot+1] # From 0th element to last element. Note: pivot start feom 0, so pivot+1.

arr = [1,1,2,2,2,3,4,4,4,5,5]
print(remove_duplicates_space(arr))



# Method - 2:
def remove_duplicates(arr):
    n = len(arr)

    if n == 0 or n ==1:
        return arr

    pivot = 0

    for last_o in range(0, n-1): # second last element
        if arr[last_o] != arr[last_o + 1]:
            arr[pivot] = arr[last_o]
            pivot = pivot+1
    arr[pivot] = arr[n - 1] # To write the last value inside.
    return arr[0:pivot+1] # From 0th element to last element. Note: pivot start feom 0, so pivot+1.

A = [1,1,2,2,2,3,4,4,4,5,5]
print(remove_duplicates(A))