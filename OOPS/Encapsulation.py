# Private - It can't be used/accessed outside the class.
# default all the variables & methods are public.

class Bank:
    def __init__(self):
        self.__value = 10 # Private Variable

    def ram(self): # Public Method
        print("Am Ram")

    def __raj(self): # Private Method
        print("Am Raj")

obj = Bank()
obj.ram()
# obj.__raj() # This 'll throw error. Bcoz it's a private method.

# Private Method should be accessed,
obj._Bank__raj()
print(obj._Bank__value)

# Protected

class A:
    def _method1(self):   # Protected Method
        print("Am a protected Method01")

class B(A):
    def __init__(self):
        self._var = 10  # Protected Variable

    def _method2(self):   # Protected Method
        print("Am a protected Method02")

obj1 = B()

print(obj1._var)
obj1._method2()
obj1._method1()