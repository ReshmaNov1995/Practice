"""
Anagram
This will give the occurrence of word's indices in the array.

Input:
arr =  ["cat", "dog", "god", "act", "tac"]

Output:
[act:3 dgo:2]
"""

def anagram(anag):
    size = len(anag)
    dict = {}

    for i in range(size):
        word = ''.join(sorted(anag[i])) # sort - ['a','c','t']['d','g','o']['d','g','o']['a','c','t',]['a','c','t']; join - act,dgo,dgo,act,act
        # print(word)
        if word not in dict:
            dict[word] = [i] # [i] - list. Bcoz more than 1 value. And only list can append.

        else:
            dict[word].append(i)
    print(dict)

anag = ["cat", "dog", "god", "act", "tac"]
anagram(anag)
