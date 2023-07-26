# Find common elements in 2 lists

# def common_Elements(list1, list2):
#     list3 = []
#     count = 0
#
#     for i in list1:
#         for j in list2:
#             if (i == j):
#                 list3.append(i)
#                 count = count+1
#     print("Common Elements are: ",list3)
#     print("Common elements in both the list is: ", count)
#
# lis1 = [10, 20, 40, 50, 80]
# list2 = [10, 30, 50, 90, 100]
#
# common_Elements(lis1, list2)

# Same logic as program_1

def method(list1, list2):
    set1 = set(list1)
    set2 = set(list2)

    common = set1 & set2
    print(common)

lis1 = [10, 20, 40, 50, 80]
list2 = [10, 30, 50, 90, 100]
method(lis1, list2)