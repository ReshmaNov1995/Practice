# Find out pairs with given sum value of an array

# arr = [5,7,4,3,9,8,19,21]
# sum = 17

# Sort the given value of an array

# Algorithm:
# if (arr[left]+arr[right] > target):
#     right = right-1 Here right move towards left
#
# elif (arr[left]+arr[right] < target):
#     left = left+1 Here left move towards right
#
# elif (arr[left]+arr[right] == target):
#     right = right - 1
#     left = left + 1

def twosum(arr, sum):
    # a = sorted(arr) # Sort in ascending order
    # print(a)
    arr.sort()
    left = 0
    right = len(arr)-1
    while (left<=right):
        if (arr[left] + arr[right] > sum): # 3,21=24; 3,19=22;
            right = right-1  # Here right move towards left. 19; 9

        elif (arr[left] + arr[right] < sum): # 3,9=12; 4,9=13; 5,9=14; 7,9=16;
            left = left+1  # Here left move towards right. 4; 5; 7; 8;

        elif (arr[left]+arr[right] == sum): # 8,9=17;
            print("Value of a pair is ", arr[left], "&", arr[right] )
            right = right - 1
            left = left + 1

arr = [5,7,4,3,9,8,19,21]
sum = 17
twosum(arr, sum)

# 3 4 5 7 8 9 19 21
# Time complexity is, T(n) = o(n log n)
# Space complexity is o(1)