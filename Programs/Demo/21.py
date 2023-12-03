"""
Extract all the number in the given string and return the number as a list

Input:
sentence = "Nancy is 90 years old. she wants 12.0232 toffees"

Output:

"""

def extract_num(sentence):
    list1 = sentence.split()
    list2 = []

    for i in list1:
        if i.isdigit():
            list2.append(i)
    print(list2)

sentence = "Nancy is 90 years old. she wants 12.0232 toffees"
extract_num(sentence)

import re
var = re.findall("\d*\.?\d+", sentence)
print(var)