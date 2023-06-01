# Example - 1: Creating Set

set1 = {"Reshma", 26, "Roja", 27}
print(set1)

# Example - 2: Accessing values of set

for i in set1:
    print(i)

# Example - 3: Value exist in Set or not

set2 = {"trojan", "malware", "zimsow"}
print("malware" in set2)
print("Reshma" in set2)


# Example - 4: Add items to Set

# add() - Add singe item
set2.add("rishen")
print(set2)

# update() - Add Multiple item
set2.update(["Reshma", "Roja", "Rishaba"])
print(set2)

# Example - 5: Set length

print(len(set2))
#
# Example - 6: Remove item from set
# Both remove() and discard() ll perform same.
# Only difference is, discard the non-existing value in the set won't throw error.

# Method - 1: remove()
set2.remove("Roja")
print(set2)

# Method - 2: discard()
set2.discard("Reshma")
print(set2)

# Example - 7: Clear the items in set

set3 = {"fear", "afraid", "unease"}
set3.clear()
print(set3)

# Example - 8: Join Set

# Method - 1: union()
set4 = {12, 98, "icecream", 652, "chocolate"}
set5 = {"temptation", "FerreroRocher", "KinderJoy"}
set6 = set4.union(set5)
print(set6)

# Method - 2: update()
set4.update(set5)
print(set4)

# Example - 9: Copy

set50 = set4.copy()
print(set4)
print(set50)