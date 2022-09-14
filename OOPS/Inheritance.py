# # Example 1: Single Inheritance
#
# class A:
#     def m1(self):
#         print("Am Method 01")
#
# class B(A):
#     def m2(self):
#         print("Am Method 02")
#
# bobj = B()
# bobj.m1()
# bobj.m2()
#
# # Example 2: Single Inheritance
#
# class A:
#     a,b = 100,200
#     def m1(self):
#         print(self.a + self.b)
#
# class B(A):
#     x,y = 500, 100
#     def m2(self):
#         print(self.x - self.y)
#
# bobj = B()
# bobj.m1()
# bobj.m2()
#
# # Example 3: Multilevel Inheritance
#
# class A:
#     a,b = 100,200
#     def m1(self):
#         print(self.a + self.b)
#
# class B(A):
#     x,y = 500, 100
#     def m2(self):
#         print(self.x - self.y)
#
# class C(B):
#     i, j = 7,9
#     def m3(self):
#         print(self.i * self.j)
#
# bobj = B()
# bobj.m1()
# bobj.m2()
#
# cobj = C()
# cobj.m1()
# cobj.m2()
# cobj.m3()

# # Example 4: Hierarchical Inheritance
#
# class A:
#     a,b = 100,200
#     def m1(self):
#         print(self.a + self.b)
#
# class B(A):
#     x,y = 500, 100
#     def m2(self):
#         print(self.x - self.y)
#
# class C(A):
#     i, j = 7,9
#     def m3(self):
#         print(self.i * self.j)
#
# bobj = B()
# bobj.m1()
# bobj.m2()
#
# cobj = C()
# cobj.m1()
# cobj.m3()
#
# # Example 5: Multiple Inheritance
#
# class A:
#     a,b = 100,200
#     def m1(self):
#         print(self.a + self.b)
#
# class B:
#     x,y = 500, 100
#     def m2(self):
#         print(self.x - self.y)
#
# class C(A,B):
#     i, j = 7,9
#     def m3(self):
#         print(self.i * self.j)
#
# cobj = C()
# cobj.m1()
# cobj.m2()
# cobj.m3()
#
# # Example 6: Method overriding
#
# class A:
#     def m1(self):
#         print("m1 from A")
#
# class B(A):
#     def m1(self): # Method overrided
#         print("m1 from B")
#
# bobj = B()
# bobj.m1() # it 'll call the method from B class which is overrided
#
# # Example 6a: In Method overriding - Methods bfr n aftr overriding has to be invoked
#
# class A:
#     def m1(self):
#         print("m1 from A")
#
# class B(A):
#     def m1(self): # Method overrided
#         print("m1 from B")
#         super().m1() # calling the super class method from a child class
#
# bobj = B()
# bobj.m1()
#
# # Example 7:
# class A:
#     a, b = 10, 20
#
# class B(A):
#     i, j = 100, 200
#     def m1(self, x,y):
#         print(x+y)
#         print(self.i + self.j)
#         print(self.a + self.b)
#
# bobj = B()
# bobj.m1(1000, 2000)

# Example 8:
import self as self


class Bank:
    def rateOfInterest(self):
        return 0

class XBank(Bank):
    def rateOfInterest(self):
        return 10

print(super(XBank).rateOfInterest)

class YBank(Bank):
    def rateOfInterest(self):
        return 20

xobj = XBank()
print(xobj.rateOfInterest())

# # Example 9: variable overriding
#
# class A:
#     name = "Reshma"
#
# class B(A):
#     name = "Roshan"
#     # If super class variable has to be accessed,
#     def test(self):
#         print(super().name)
#
# bobj = B()
# print(bobj.name)
# bobj.test()

# -----DOUBT-----
