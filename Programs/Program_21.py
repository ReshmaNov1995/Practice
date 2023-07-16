# Given a string. Extract all the number in the string and return the number as a list
# Input - "I am 89 years old. My father name is 120 "
# Output - [89,120]


sentence = "Nancy is 90 years old. she wants 12.0232 toffees"
num = []

for words in sentence.split():
    if words.isdigit(): # This will work only for non-decimal
        num.append(words)
print(num)

# Decimal Values - Regex concept -> regexr.com
# d - digit
# + -> 1 or more
# * -> 0 or more
# ? -> o or 1


import re
digit = re.findall("\d*\.?\d+", sentence)
print(digit)