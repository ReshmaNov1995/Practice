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
    # global ab = 200 incorrect syntax both declaration and initialisation cannot be declared in same line. Though it is a global declaration.
    ab = 100
    print(ab) # 100

fun1()
print(ab) # 100


# Example - 4:

xy = 300

def fun2():
    global xy
    xy = 500
    print(xy)

# fun2() if the function is not called then body of the function will not be considered
print(xy)
