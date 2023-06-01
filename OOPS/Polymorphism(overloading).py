# Example 1:

class A:
    def m1(self, name = None):
        if name != None:
            print("Hello " + name)

        else:
            print("Hello")
a = A()
# Same method is used with diff arguments
a.m1()
a.m1("Reshma")

# Example 2

class A:
    def m1(self, a=1, b=1, c=1):
        print(a+b+c)

a = A()
a.m1()
a.m1(10,20)
a.m1(10,20,30)


# Example 3 - Method overloading is not possible here like java. The latest method only considered. First method is not supposed to be accessed.

class A:
    def m1(self, a):
        print("A")

    def m1(self, a, b):
        print("B")

a = A()
a.m1(1,2)
# a.m1(1) #this 'll throws the error. Bcoz it is expecting for 2 arguments.

# For java like Method overloading concept, this below approach can be followed

from multipledispatch import dispatch

@dispatch(int, int) # datatype declaration
def name(a,b):
    print("this is first method")

@dispatch(str,str,int)
def name(a,b,c):
    print("this is second method")

name(1,2)
name("Reshma", "Roja", 6)


