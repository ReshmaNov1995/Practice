"""
Find Missing number in an array

arr = [12,14,15,16,17,18]
"""

def miss_num(arr):
    n = arr[-1]
    total = n*(n+1)//2
    sum1 = sum(arr)
    print(total-sum1)

arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17]

miss_num(arr)