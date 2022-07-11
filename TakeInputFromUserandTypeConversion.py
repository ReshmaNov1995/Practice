a = input("Enter Number1:")
b = input("Enter Number2:")

print(type(a))
print(type(b))

print(a+b)

# Note: Value getting from Console always a String datatype.
# So, Concatenation occurred here.
# To avoid this, whenever passing input from console specify it along with the required datatype.

# Approach 1
num1 = int(input("Enter Number1:"))
num2 = int(input("Enter Number2:"))

print(num1+num2)

# Approach 2
a = input("Enter Number1:")
b = input("Enter Number2:")

print(int(a)+int(b))