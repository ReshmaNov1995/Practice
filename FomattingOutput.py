# name = 'Reshma'
# age = 26
# sal = 5325.50

# Approach 1
name,age,sal = 'Reshma',25,5325.50

print(name,age,sal)

# Approach 2
print("Name is:",name)
print("Age is:",age)
print("Salary is:",sal)

# Approach 3 %
# %s-string %d-digit %g-decimal
print("Name is:%s Age is:%d Salary is:%g" %(name,age,sal))

# Approach 4 {}
# Formatting 'll b happened in sequential manner
print("Name is:{} Age is:{} Salary is:{}" .format(name,age,sal))

print("Age is:{} Name is: {} Salary is: {}".format(age, name, sal))

