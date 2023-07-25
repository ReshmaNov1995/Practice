"""
Convert 2 lists into dictionary; Convert dictionary to tuple

Input:
list1 = ["Reshma", "Roja", "Rishabha"]
list2 = [23,25,27]

Output:
dict1 = {Reshma:23, Roja:25, Rishabha:27}
"""

# def list_dict():
#     list1 = ["Reshma", "Roja", "Rishabha"]
#     list2 = [23, 25, 27]
#
#     list_to_dict = dict(zip(list1,list2))
#
#     print(list_to_dict)
#
# list_dict()

def dict_tup():
    dict1 = {"Reshma": 23, "Roja": 25, "Rishabha": 27}
    tuple1 = ()
    for i in dict1.items():
        # print(i)
        tuple1 = tuple1+i
    print(tuple1)

dict_tup()