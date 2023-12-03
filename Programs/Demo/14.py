"""
Rotation of String

Input:
str = "Reshma"

Output:
eshmaR
shmaRe
hmaRes
maResh
aReshm
Reshma
"""

def rotation_string(str):
    str1 = list(str)
    size = len(str1)

    for i in range(size):
        str1.pop(0)
        str1.append(str[i])
        print(''.join(str1))


str = "Reshma"

rotation_string(str)