# Maximum & Minimum of the element

# def maximum(arr):
#     max = arr[0]
#     size = len(arr)
#
#     for i in range(size):
#         if arr[i] > max:
#             max = arr[i]
#
#     return max
#
# A = [63, 54, 98, 34, 89, 42, 18]
# print(maximum(A))


def minimum(arr):
    min = arr[0]
    size = len(arr)

    for i in range(size):
        if arr[i] < min:
            min = arr[i]

    return min

A = [63, 54, 98, 34, 89, 42, 18]
print(minimum(A))