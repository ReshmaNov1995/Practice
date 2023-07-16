# Reverse a list

# reverse()
# slicing
# reversed()
# loop

# # Method - 1:
# list1 = [2,8,6,9,10]
# list1.reverse()
# print(list1)
#
# # Method - 2:
# list2 = [8,62,7,54,100]
# list3 = list2[::-1]
# print(list3)
#
# # Method - 3:
# # list4 = reversed(list2) # <list_reverseiterator object at 0x000001EFEE507BE0>
# list4 = list(reversed(list2))
# print(list4)

# Method - 4:
list5 = [3,4,7,9,10]
list6 = []
for i in range(len(list5)-1, -1, -1):
    list6.append(list5[i])
print(list6)