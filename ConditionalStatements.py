# if
age = 10
if age>=12:
    print("Age is valid")


# if...else
# Example 1
age = 20
if age>=25:
    print("Age is Valid:{}" .format(age))

else:
    print("{} is Invalid Age" .format(age))

# Example 2
if False:
    print("Condition is True")
else:
    print("Condition is False")

# Example 3
if 0:
    print("True")
else:
    print("False")

# Example 4 Finding even or odd concept-> num%2=0
num=21
if num%2==0:
    print("Given num is even")
else:
    print("Given num is odd")

# Example 5 if...else in single line (ternary operator)
print("Even Number") if num%2==0 else print("Odd Number")

# Example 6 if...else multiple statements in Single line (ternary operator)
a = 20
# print("hi","python") if a>=10 else print("hello","java")
{print("hi"),print("python")} if a>=10 else {print("hello"),print("java")}

# Example 7 Multi Conditions using elif
# weekno=7
a = int(input("Enter weekno:")) 

if a==1:
    print("Sunday")

elif a==2:
    print("Monday")

elif a == 3:
    print("Tuesday")

elif a == 4:
    print("Wednesday")

elif a == 5:
    print("Thursday")

elif a == 6:
    print("Friday")

elif a == 7:
    print("Saturday")