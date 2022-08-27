# 2 types of parameters/arguments can be passed in function.
# 1)Positional Argument
# 2)Keyword Argument

# Example - 1:

def function(i,j):
    print(i,j)

function(10,20) #Positional Argument
function(j = 20, i = 50) #Keyword Argument - > 20 is assigned to j and 50 is assigned to i


# Example - 2: Default values assigned to positional arguments

def function1(i, j=10): # default value of j is 10
    print(i,j)

function1(100)
function1(100,200) # Though the j value is passed over here. Default value ll be replaced.


# Example - 3: Keyword Arguments

def function2(name, place):
    print("My name is "+name+"\nAm from "+place)

function2(name="Reshma", place="Chennai")


# Example - 4:

def function3(a,b,c):
    print(a,b,c)

#function3(11, b=20, 33)  #Syntax Error. This is wrong, As positional argument must appear before any keyword argument
#function3(10, 20, b = 30) #Logical Error. Got Multiple values for argument b
function3(11, b=20, c=33)


# Example - 5: Function can return multiple values

def largest(a, b):
    if a>b:
        return a,b
    else:
        return b,a

print(largest(20,10))
print(largest(50,60))