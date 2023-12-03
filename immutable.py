

# docstring - Defining about the code in document form. It is used to specify about the functionality of a method/function.
"""
Mutable - list, dictionary, set
Immutable - numeric, string, tuple
"""

# list
# a = [1,2,3]
# print(id(a))
# a[1] = 4
# a.append("5")
# print(a)
# print(id(a)) # 500
# b = a
# b[1] = 7
# print(b)
# print(id(b)) # 500
# print(a)

# string
# b1 = "Hello"
# print(id(b))
# b[1] = "a"
# print(b)
# c1 = b1
# c1 = c1+"Hi"
# print(c1)
# print(b1)


# tuple
# c = (1,2,3)
# c[1] = 4
# print(c)

# numeric
# d = 123
# d[1] = 4
# print(d)

# q = "Hello"
# print(id(q))
# q = q+"Hi"
# print(id(q))

# Ex: Mutable # List
a = [100, 300]
# b is a reference variable of a
b = a
# If there is change in reference variable's value(b). It 'll affect the original value.
b[1] = 200
print(b)
print(a)

# Ex: Immutable # Tuple
a = (10, 20)
# b is a copy variable of a
b = a
c = (40, 50)
# If there is change in reference variable's value(b). It 'll not affect the original value.
b = b+c
print(b)
print(a)


l = (10, 20, 30)
print(l)
# l[1] = 100
l = (300)
print(l)