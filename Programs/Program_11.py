# Maximum Sum of Subarray

# Algorithm
# curr_sum = 0
# max_so_far = a[0] first element in the array
# st = 0, en = 0, poi = 0
# for i in range(o, size):
#     curr_sum = curr_sum+a[i]
#     if max_so_far<curr_sum:
#         st = poi, end = i
#         max_so_far = curr_sum
#     if curr_sum < 0: When the same value is negative. It will takes as (0)zero automatically.
#         curr_sum = 0
#           poi = i + 1
# poi -  defines the starting comparison value's index. end - defines the ending comparison value's index.
# Finally start index is 3 and end index is 8. While calculate those index value will get the max sum as 7.

def max_sum_subarray(arr):
    size = len(arr)
    curr_sum = 0
    max_so_far = arr[0]
    st = 0; end = 0; poi = 0
    for i in range(0, size):
        curr_sum = curr_sum + arr[i]
        if max_so_far<curr_sum:
            max_so_far = curr_sum
            st = poi; end = i
        if curr_sum < 0:
            curr_sum = 0
            poi = i + 1

    print("Maximum sum of Sub Array is", max_so_far)
    print("Start index of window is", st)
    print("End index of window is", end)

A = [4, -3, -2, 2, 3, 1, -2, -3, 6, -6, -4, 2, 1]
max_sum_subarray(A)