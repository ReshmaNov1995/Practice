"""
Find Missing number in an array

Input:
list1 = [1,2,3,5,6,7]

Output:
4
"""

# Method - 1: Summation Method
# Summation n*(n+1)/2 - Sum(A)
# 7*(8)/2 - 1+2+4+5+6+7
# 28 - 25 = 3. 3 is a missing number.


def get_missing_summation(a):
    n = a[-1]
    total = n*(n+1)//2
    sum1 = sum(a)
    print(total-sum1)


a = [3, 4, 5, 6, 7, 8, 9, 10, 12]
get_missing_summation(a)