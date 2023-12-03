"""
Find out pairs with given sum value of an array

Input:
arr = [10,20,30,40,50,60]
sum = 60

Output:
10 50

"""

def pairs(list1):
    size = len(list1)
    for i in range(size):
        for j in range(size):
            if arr[i]+arr[j] == sum:
                print(arr[i],arr[j])

arr = [10, 20, 30, 40, 50, 60]
sum = 60


pairs(arr)