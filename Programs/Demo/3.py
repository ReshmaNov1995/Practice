"""
Convert 2 lists into dictionary; Convert dictionary to tuple

Input:
list1 = ["Reshma", "Roja", "Rishabha"]
list2 = [23,25,27]

Output:
dict1 = {Reshma:23, Roja:25, Rishabha:27}
"""

# def list_dict(list1, list2):
#     dict1 = dict(zip(list1, list2))
#     print(dict1)
#
# list1 = ["Reshma", "Roja", "Rishabha"]
# list2 = [23,25,27]
#
# list_dict(list1, list2)


def dict_tup(dict1):
    tuple1 = tuple()
    for i in dict1.items():
        tuple1 = tuple1+i
    print(tuple1)

dict1 = {"Reshma":23, "Roja":25, "Rishabha":27}

dict_tup(dict1)
