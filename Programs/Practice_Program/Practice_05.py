"""
Find out pairs with given sum value of an array

Input:
arr = [10,20,30,40,50,60]
sum = 60

Output:
10 50

"""

def pair_sum(arr, sum):

    arr1 = sorted(arr)
    # print(arr1)
    size = len(arr1)

    for i in range(size):
        for j in range(size):
            if arr[i]+arr[j] == sum:
                print("Sum of array is ", arr[i],arr[j])

arr = [30,40,10,50,60,20]
sum = 60

pair_sum(arr, sum)