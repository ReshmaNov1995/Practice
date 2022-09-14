# # Example 1:
#
# class A:
#     def m1(self, name = None):
#         if name != None:
#             print("Hello " + name)
#
#         else:
#             print("Hello")
# a = A()
# # Same method is used with diff arguments
# a.m1()
# a.m1("Reshma")

# Example 2

class A:
    def m1(self, a=1, b=1, c=1):
        print(a+b+c)

a = A()
a.m1()
a.m1(10,20)
a.m1(10,20,30)

# -----DOUBT-----