"""
Anagram

Input:
arr =  ["cat", "dog", "god", "act", "tac"]

Output:
[act:3 dgo:2]
"""

def anagram(list):
    list2 = []

    for i in list:
        list2.append(sorted(i))

    print("list2", list2)
    list3 = []
    for i in list2:
        list3.append(''.join(i))
    print(list3)

    dict = {}

    for i in range(len(list3)):
        if list3[i] not in dict:
            dict[list3[i]] = 1

        else:
            dict[list3[i]] = dict[list3[i]] + 1

    print(dict)

arr =  ["cat", "dog", "god", "act", "tac"]
anagram(arr)