"""
Anagram
This will give the occurrence of word's indices in the array.

Input:
arr =  ["cat", "dog", "god", "act", "tac"]

Output:
[act:3 dgo:2]
"""


def anagram(arr):
    size = len(arr)
    dict = {}

    for i in range(size):
        word = ''.join(sorted(arr[i]))

        if word not in dict:
            dict[word] = 1

        else:
            dict[word] = dict[word]+1

    print(dict)

arr = ["cat", "dog", "god", "act", "tac"]

anagram(arr)