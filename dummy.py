# def fun(a,b,c):
#     i = a+b
#     j = b+c
#     return i,j
#
# print(fun(10,20,30))

class Data:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Data(self.value + other.value)


a = Data(40)
# b = Data(2)
# c = a + b

print(a)
# 42
