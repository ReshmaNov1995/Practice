# Example 1: Creating dictionary

dict1 = {1:"Reshma", 2:"Roja", 3:"Rekha", 4:"Ranjith"}
print(dict1)

# Example 2: Accessing Item from dictionary

# Method - 1:
dict2 = {"Name": "Roja", "Year": 1995, "Month": "September", "Passing": 2017}
print(dict2["Month"])

# Method - 2: using get()
print(dict1.get(2))

# Example 3: Change values in dictionary

dict1[3] = "Reeta"
print(dict1)

# Example - 4: Reading items from dictionary using loop

# Printing keys
for i in dict1:
    print(i)

# Printing values
for i in dict1:
    print(dict1[i])

# Printing values using values()
for i in dict1.values():
    print(i)

# To Print keys along with Values - items()
for x,y in dict1.items():
    print(x,y)

# Example 5: Check key exist in dictionary

if 2 in dict1:
    print("Exist")
else:
    print("Not Exist")

# OR

print(2 in dict1)

# Example 6: Find number of items in dictionary

print(len(dict2))

# Example 7: Adding Items in dictionary

dict1[5] = "Rakul"
print(dict1)

# Example 8: Remove Item from dictionary

# Method - 1: using pop()
dict1.pop(3)
print(dict1)

# Method - 2: del keyword
del dict1[4]
print(dict1)

# del dict1
# print(dict1)

#  Example 9: Clear items in the dictionary

# dict2.clear()
# print(dict2)

# Example 10: Copy dictionary

# Method - 1: without using copy
# dict2 = dict1
print(dict2)
print(dict1)

# Method - 2:  copy
dict1 = dict2.copy()
print(dict1)
