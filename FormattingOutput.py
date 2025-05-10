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


# Approach 5
# %f-float (float 'll change the value to decimal even it is number).
# .2f (It 'll display 2 digits after the digit passed)

txt = "I have {an:s} Rupees!"
print(txt.format(an = "kk's"))

txt = "I have {an:d} Rupees!"
print(txt.format(an = 6))

# txt = "I have {an:f} Rupees!"
txt = "I have {an:.2f} Rupees!"
print(txt.format(an = 6))

txt = "I have {an:g} Rupees!"
print(txt.format(an = 6.2))
