# Prime Number

from math import sqrt

def prime_num(num):
    if (num>1):
        for i in range(2, int(sqrt(num))+1):
            if num%i == 0:
                return False
        return True

isprime = prime_num(47)
if isprime:
    print("Prime Number")
else:
    print("Not a Prime Number")