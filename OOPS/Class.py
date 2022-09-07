# creating a class
class MyClass:
    def methodcase(self): # self is a default argument taken by method which represents the class name
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

