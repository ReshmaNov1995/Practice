"""
Factorial of a number

Input:
5

Output:
5*4*3*2*1
"""

def factorial(n):
    temp = 1

    for i in range(1, n+1):
        temp = i*temp # 1*1; 2*1; 3*2; 4*6; 5*24
    print(temp)

n = 5
factorial(n)