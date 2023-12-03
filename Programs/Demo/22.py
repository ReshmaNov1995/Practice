"""
Fibonacci series

Input:
5

Output:
0 1 1 2 3
"""

def fibbo(fib):
    first = 0
    second = 1
    print(first, second, end=" ")

    for i in range(2, fib):
        next = first+second
        first = second
        second = next
        print(next, end=" ")

fib = 5

fibbo(fib)