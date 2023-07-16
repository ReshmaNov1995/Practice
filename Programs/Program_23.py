# Factorial of number

#5*4*3*2*1

def fact(n):
    temp = 1
    for i in range(1, n + 1):
        temp = i * temp
    print("factorial of", n, "is", temp)


n = 5
fact(n)

