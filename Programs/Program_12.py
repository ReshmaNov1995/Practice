# Anagram
# Which means same letter with different words

# Algorithm
# Create a dictionary
# If sorted word not in dictionary,
#     # set words as key & index as value
# If sorted word in dictionary,
#     append index for word

# [cat, dog, god, act, tac]

def anagram(A):
    if A == None:
        return
    else:
        dict = {}
        for i in range(len(A)):
            word = ' '.join(sorted(A[i]))
            # word = sorted(A[i])
            # print(word)
            if word not in dict:
                dict[word] = [i+1]
            else:
                dict[word].append(i+1)
        return dict

arr =  ["cat", "dog", "god", "act", "tac"]
print(anagram(arr)) # This will print the occurrence of word's indices