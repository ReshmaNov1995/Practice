"""
Input:
a = "reshma"
b = "roja"
Find common letters b/w 2 strings

Output:
r,a
"""

def common_letter():
    str1 = input("Enter the first String:")
    str2 = input("Enter the second String:")

    str01 = set(str1)
    str02 = set(str2)
    print(str01, str02)

    common_letters = str01 & str02

    print(common_letters)


common_letter()