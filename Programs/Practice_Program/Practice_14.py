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

def rotation(str):
    size = len(str)
    list1 = list(str)


    for i in range(size):
        list1.pop(0)
        list1.append(str[i])

        print(''.join(list1))

str = "Reshma"
rotation(str)