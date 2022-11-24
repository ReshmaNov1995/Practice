# Example 1: Create list1

list1 = list() # empty list1
list11 = [10,20,58,90,100]
list12 = ["Reshma", "Roja", "Sangeetha"]
list13 = [20,"Ramya",56.20,"Rechal"]

print(list1, list11, list12, list13)

# Example 2: Accessing Items from the list1

# Negative index starts from right to left

list1 = [545,"fgf",65,"dfgdt",99]

print(list1[0], list1[3], list1[4], list1[-3])

# Example 3: Range of Index
# greater and lesser combination with same negative/positive integers, equal values 'll give empty list.
list1 = ["Apple", "Orange", "Banana", "PineApple", "Guava", "Jackfruit", "Grapes"]

print(list1[1:5])
print(list1[-1:-5])
print(list1[1:1])
print(list1[5:1])

# Example 4: Change Item Value

list1 = ["pen", "ball", "paper", "sketch", "stapler"]
print(list1)
list1[2] = "pen"
print(list1)

# Example 5: Read the list1 item using loop

list1 = ["Anita", "Ankita", "Archana", "Aakash", "Abhishek", "Abhimaneu"]
for i in list1:
    print(i)

# Example 6: Check if the item is exist in the list

list1 = ["Carrot", "Beetroot", "LadysFinger", "Raddish","Drumstick"]

if "Potato" in list1:
    print("Potato is present")
else:
    print("Potato is absent")

# Example 7: list length

list1 = [23,464,36,36, "Reeta", "Rekha", "Sharmi"]
print(len(list1))

# Example 8: Add Items in the list
# append() Adding the new item at the end of the list1.
# insert() Adding the new item at the required index.

list1 = ["Vijay", "wilson", "irfan", "Jonathan", "Sringada"]
list1.append("Reshma")
print(list1)

list1.insert(1, "Reshma")
print(list1)

# Example 9: Remove item from the list1
# Method - 1: pop()
list1 = ["rohit", "sharma", "priyanka", "chopra", "deepika", "padugon"]
list1.pop(2)
print(list1)

# Method - 2: del keyword
list1 = ["12reshu", "Kavika65", "Renuka89", "Revathy32"]
del list1[1]
print(list1)

# Method - 3: clear() - will clear all the values of the list1
list1 = ["Raichal", "Sharmi", "Srinidhi", "Venkatesh", "Vishal"]
list1.clear()
print(list1)

# Example 10: copy

# Method - 1: list(listtobecopied)
list1 = ["aws", "sds", "des", "opr", "srt"]
list2 = list(list1)
print(list1)
print(list2)

# Method - 2: copy()
list1 = [56,99,98,75,56,89,56,59]
list2 = list1.copy()
print(list1)
print(list2)

# Example 11: Join List

# Method - 1: using + operator
list1 = ["ab", "bc", "ca", "ac"]
list2 = [32,56,75,84,10,21]
list4 = list1+list2
print(list4)

# Method - 2: using loop
for i in list2:
    list1.append(i) # while use only append. It'll create like [s,s,s[c,r,cr]]
print(list1)

# Method - 3: using extend()
list5 = ["ref", "trf", "ytr", "vty", "vfr"]
list6 = ["de", "dewd", "dee", "esf"]
list5.extend(list6)
print(list5)

# Example - 12: Compare 2 lists

if list5 == list6:
    print("list is equal")
else:
    print("list is not equal")

print(list6[-2])  # Negative index
