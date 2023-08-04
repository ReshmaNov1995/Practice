"""
Fibonacci series

Input:
5

Output:
0 1 1 2 3
"""

def fibonacci(num):
    first = 0
    second = 1
    print(first, second, end=" ")

    for i in range(2,num):
        next_num = first + second
        first = second
        second = next_num
        print(next_num, end=" ")

n = int(input("Enter Number:"))
fibonacci(n)