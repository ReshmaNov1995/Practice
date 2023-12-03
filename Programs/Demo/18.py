"""
Prime Number

"""

def prime(lower, upper):

    for num in range(lower, upper+1):
        if num > 1:
            for i in range(2, int(num)):
                if (num % i) == 0:
                    break

            else:
                print(num, "is a Prime")

        else:
            print("Not a Prime")

# num = 57

prime(11, 19)