# Example 1: Creating tuple

tuple1 = ("Reshma", "Roja", "Meera", "Archana", "Aakash", "Naveen")
print(tuple1)

print(tuple()) # Empty tuple

# Example 2: Accessing tuple

tuple1 = ("Kavya", "Keerthana", "Kannika", "Kavin", "kaalya")
print(tuple1[4])
print(tuple1[-2]) # Negative index

# Example 3: Range of Index
# greater and lesser combination with same negative/positive integers, equal values 'll give empty tuple.
tuple1 = ("Apple", "Orange", "Banana", "PineApple", "Guava", "Jackfruit", "Grapes")

print(tuple1[1:5])
print(tuple1[-3:-1])
print(tuple1[3:1])
print(tuple1[2:2])

# Example 4: Change Item Value
# By default tuple does not allow to change value bcoz it is immutable. But, there is a workaround.
# tup->list(modify)->tup

tup1 = ("reshma", "ravi", "raja", "ranjith", "rohan")
print(tup1)
list1 = list(tup1) # tuple to list
print(list1)
list1[2] = "roja" # changing index value
print(list1)
tuple2 = tuple(list1) # list to tuple
print(tuple2)

# Example 5: Read the tuple item using loop

tuple1 = ("Anita", "Ankita", "Archana", "Aakash", "Abhishek", "Abhimoneu")
for i in tuple1:
    print(i)

# Example 6: Check if the item is exist in the tuple

tuple1 = ("Carrot", "Beetroot", "LadysFinger", "Raddish","Drumstick")

if "Beetroot" in tuple1:
    print("Beetroot is present")
else:
    print("Beetroot is absent")

# Example 7: tuple length

tuple1 = (23, 56, 79, 99 )
print(len(tuple1))

# Example 8: Add Items in the tuple
# By default tuple does not allow to Add Item bcoz it is immutable. But, there is a workaround.
# Convert into list and Add items

# Example 9: Copy

# Method - 1:
tuple2 = tuple(tuple1)
print(tuple1)
print(tuple2)

# Method - 2:
tuple3 = tuple1
print(tuple1)
print(tuple3)


# Example - 10: Removing item from tuple - Impossible bcoz tuple is immutable
#
# del keyword
# del tuple1

# Example - 11: Joining tuple

# Method - 1: using + operator
tuple1 = ["ab", "bc", "ca", "ac"]
tuple2 = [32,56,75,84,10,21]
tuple5 = tuple1+tuple2
print(tuple5)

# Example - 12: Compare 2 tuple

if tuple1 == tuple2:
    print("tuples are equal")
else:
    print("tuples are not equal")