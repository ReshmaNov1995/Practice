"""
Extract all the number in the given string and return the number as a list

Input:
sentence = "Nancy is 90 years old. she wants 12.0232 toffees"

Output:

"""

# def extract_num(sentence):
#     list1 = sentence.split()
#
#     for i in list1:
#         if i.isdigit():
#             print(i)
#
sentence = "Nancy is 90 years old. she wants 12.0232 toffees"
# extract_num(sentence)

import re
list1 = []
num = re.findall("\d*\.?\d+", sentence)
print(num)

# Decimal Values - Regex concept -> regexr.com
# d - digit
# + -> 1 or more
# * -> 0 or more
# ? -> o or 1