# Rotation of String

# Algorithm
# concatenate string with itself
# Traverse the concatenated string from 0 to size -1
# print all string

# Left Rotated String

def left_rotatedstring(name):
    size = len(name)

    temp = name + name
    for i in range(size+1):
        for j in range(size):
            print(temp[i + j], end= "")

        print()

A = "NETSET"
left_rotatedstring(A)

# Rotation String - Two strings are rotated with each other

def checkrotation(str1, str2):
    if len(str1) != len(str2):
        return False
    size = len(str1)
    s = str1+str1

    if str2 in s:
        print(str1, "is matching with", str2)

    else:
        print(str1, "is not matching with", str2)

checkrotation("ANU", "NUA")