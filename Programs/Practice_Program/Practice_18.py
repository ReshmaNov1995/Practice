"""
Prime Number

Input:

"""


def prime(num):

    if (num>1):
        for i in range(2, int(num/2)+1): # If num is divisible by any number between. 2 and n / 2, it is not prime
            if num%i == 0:
                print(num, "is not a Prime")
                break

        else:
            print(num, "is a Prime")
    else:
        print(num, "is not a Prime")

num = 10
prime(num)