# creating a class
# Example 1:

class MyClass:
    def methodcase(self): # Instance Method - self is a default argument taken by method which represents the instance of a class. Static Method will consider as a argument alone.
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

# Static Method, Class Method & Instance(Non-Static) Method
# Example 2:

class Static:
    def imethod(self):
        print("Am Instance Method")
    @classmethod
    def kmethod(cls):
        print("Am Class Method")
    @staticmethod
    def smethod():
        print("Am Static Method")

# Invoke methods by class name
Static.smethod()
Static.kmethod()

# Invoke methods by Object
s = Static()
s.imethod()
# Static.imethod(s)  # Instance method can also invoke like this. But value has to be passed for the self.
s.kmethod()
s.smethod()

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

# Example 6:
# Constructor

class ConstClass:
    def __init__(self):
        print("Am a Constructor")

    def method(self):
        print("Am a Method")

cc = ConstClass() # Here constructor ll be called while the object is created
cc.method()

# Example 7:
# Parameterized Constructor

class ParaConst:
    name = 'Reshma'
    def __init__(self, name):
        print(name)
        print(self.name)

pc = ParaConst('Krishnan')

# Example 8:
# Employee Details - Constructor: eid, name, sal Method: print eid, name, sal

class Employee:
    # eid, name, sal = "", "", ""

    def __init__(self, eid, name, sal):
        self.eid = eid # In this case line 125 is not required
        self.name = name
        self.sal = sal

    def method(self):
        print(self.eid, self.name, self.sal)

emp1 = Employee(1,"Reshma", 8600000)
emp1.method()

emp2 = Employee(2, "Rishaba", 9500000)
emp2.method()

emp3 = Employee(3, "Rekha", 9856000)
emp3.method()

# Example 9:
class Employee:
    # eid, name, sal = "", "", ""

    def __init__(self, eid, sal, name):
        self.eid = eid
        self.name = name
        self.sal = sal

    def __str__(self):
        return self.name

    def __float__(self): # Passing list of values throws error
        return self.sal

    def __int__(self):
        return self.eid


emp1 = Employee(121, 25462.00, "Reshma")
print(str(emp1))
print(float(emp1))
print(int(emp1))