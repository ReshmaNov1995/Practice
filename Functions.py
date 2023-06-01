# A Function can be called 'n' no.of.times.

# Example 1:

# Declaring a function
def function1():
    print("Welcome to Automation") # Body of the function

# Calling a function
function1()

# Example 2: Function with Parameter

def function2(name):
    print("Welcome to Automation "+name)

function2("Reshma")

# Example 3: Function with Multiple Parameter

def function3(val1,val2):
    a = val1+val2
    return a
print(function3(30,20))

# Example 4: Function without parameter and no return value

# Method - 1:
def function4():
    return
print(function4()) # It 'll return none

def function4a():
    i = 20
    print(i)
    return
print(function4a())

# Method - 2: Function with parameter and no return value
def function4a(a):
    i = 20+a
    return
print(function4a(10))

# Example 5:

# Method - 1:
def function5(a,b):
    print(a+b)

function5(20,30)

# Method - 2:
def function5a(a,b):
    return (a+b)

print(function5a(20,30))
