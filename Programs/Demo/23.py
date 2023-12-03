"""
Factorial of a number

Input:
5

Output:
5*4*3*2*1
"""

def fact(num):
    temp = 1
    for i in range(1, num+1):
        temp = i*temp
    print(temp)

num = 5
fact(num)