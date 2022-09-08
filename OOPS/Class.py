# creating a class
# Example 1:

class MyClass:
    def methodcase(self): # Instance Method - self is a default argument taken by method which represents the class name. Static Method will consider as a argument alone.
        pass
    def methodcase1(self):
        print("Am Method Case 1")
    def methodcase2(self, Age):
        print(Age)

# Object Representation
# Reference variable = ClassName()
# A Class can have 'n' no.of.Objects

mc = MyClass()
mc1 = MyClass()
mc2 = MyClass()

mc.methodcase()
mc.methodcase1()
mc.methodcase2(23)

mc1.methodcase()
mc1.methodcase1()
mc1.methodcase2(24)

mc2.methodcase()
mc2.methodcase1()
mc2.methodcase2(25)

# Static Method & Non-Static(Instance) Method
# Example 2:

class Static:
    def imethod(self):
        print("Am Instance Method")
    @staticmethod
    def smethod(self):
        print()


Static.smethod(1)

s = Static()
s.smethod(30)

# Example 3:
# Class Variable

class Class:
    a, b = 10, 20
    def add(self):
        print(self.a + self.b) # class variable must accessed inside a method by using self keyword

c = Class()
c.add()

# Example 4:
# Diff b/w Global, Class & Local Variable

i, j = 20, 30 #Global Variable
class VariableClass:
    a, b = 10, 20 #Class Variable
    def method(self):
        x, y = 50, 100 #Local Variable
        print(x + y)
        print(self.a + self.b)
        print(i + j)

vc = VariableClass()
vc.method()

# Example 5:
# Global, Class & Local Variable with same name

m, n = 20, 30 #Global Variable
class VariableClass1:
    m, n = 10, 20 #Class Variable
    def method(self):
        m, n = 50, 100 #Local Variable
        print(m + n) #local
        print(self.m + self.n) #class
        print(globals()['m'] + globals()['n']) #global

vc = VariableClass1()
vc.method()