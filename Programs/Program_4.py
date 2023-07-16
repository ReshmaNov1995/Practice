# Find 1 Missing number in an array
# Array number is [1,2,4,5,6,7]

# Method - 1: Summation Method
# Summation n*(n+1)/2 - Sum(A)
# 7*(8)/2 - 1+2+4+5+6+7
# 28 - 25 = 3. 3 is a missing number.


def get_missing_summation(a):
    n = a[-1]
    total = n*(n+1)//2
    sum1 = sum(a)
    print(total-sum1)


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]
get_missing_summation(a)

# Method - 2: XOR Method
# Same input will leads to zero. Otherwise the input.
# A	B	XOR
# 0	0	0
# A	A	0
# B	B	0
# 0	A	A
# B	0	B

# XOR of 'n' natural num and numbers present in array
# 0+0+0+0+0+0+3 -> 3

# Method - 2:

# def get_missing_xor(a):
#     n = len(a)
#     xor_a = a[0]
#     for index in range(1, n):
#         xor_a = xor_a^a[index]
#     x2 = 0
#     for index in range(1, n+2):
#         x2 = x2^index
#     print(xor_a^x2)
#
# a = [1, 2, 4, 5, 6, 7]
# get_missing_xor(a)