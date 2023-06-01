# Example - 1: Common Except
from colorama import *

print("Hi Am Reshu")

# try:
#       print(a)
#
# except Exception as e:
#         # e is a name error. It can't be concatenated with String.
#         b = str(e)
#         print(Fore.RED,"Am a Exception "+b)
#         print(Style.RESET_ALL)

print("Hi Am Moorthy")

# Example - 2: Particular Except

try:
        print(10/0)

except Exception as ZeroDivisionError: # This block 'll not handle other exceptions.
        z = str(ZeroDivisionError)
        print(Fore.RED, "Am a Exception "+z)
        print(Style.RESET_ALL)

print("Exception Handled")


# Example - 3: Multiple Except ---> try, except, else, finally

try:
        num1, num2 = 10, 0
        result = num2/num1
        print(result)

except ZeroDivisionError:
        i = str(ZeroDivisionError)
        print(Fore.RED, "Am a ZeroDivisionError "+i)

except SyntaxError:
        j = str(SyntaxError)
        print("Am a SyntaxError "+j)

except OverflowError:
        k = str(OverflowError)
        print("Am a OverflowError "+k)

else:
        print(Style.RESET_ALL, "Exception not occured")

finally:
        print(Style.RESET_ALL, "Always Execute")

# Example - 4: Raise our new Exception

def enterNum(num):
        if num==0:
                raise Exception("zero is not allowed")
                # raise ValueError("ValueError has occurred")
        if num % 2 == 0:
                print("Am a even")
        else:
                print("Am a odd")


p = 0
enterNum(p)

print("Program Completed")