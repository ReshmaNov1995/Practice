"""
Prime Number

Input:

"""


def prime(num):

    if (num>1):
        for i in range(2, int(num)+1): # If num is divisible by any number between. 2 and n / 2, it is not prime
            if num%i == 0:
                print(num, "is not a Prime")
                break

            else:
                print(num, "is a Prime")
                break
    else:
        print(num, "is not a Prime")

num = 13
prime(num)

"""
Python program to display all the prime numbers within an interval
"""


lower = 11
upper = 19


for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)