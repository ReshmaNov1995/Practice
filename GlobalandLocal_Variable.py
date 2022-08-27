# # Example - 1:
#
# a = 20
#
# def fun():
#     print(a)
#
#     b = 30
#     print(b)
#
# fun()
#
# # print(b) # It throws error bcoz it's a local variable.

# # Example - 2:
#
# # Both Global and Local variable has same name. Inside the function Local variable 'll be considered.
#
# ab = 50
#
# def fun1():
#     ab = 100
#     print(ab)
#
# fun1()

# Example - 3:

ab = 50

def fun1():
    global ab # Local variable is mentioned as a global variable
    ab = 100
    print(ab) # 100

fun1()
print(ab) # 100

