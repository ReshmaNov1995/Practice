"""
Find common letters b/w 2 strings
str1 = "Reshma"
str2 = "Roja"
"""

def common_letter(str1,str2):
    set1 = set(str1)
    set2 = set(str2)

    common = set1 & set2
    print(common)


str1 = "Reshma"
str2 = "Roja"

common_letter(str1, str2)