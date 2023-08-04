# Anagram
# Which means same letter with different words
# This will give the occurrence of word's indices in the array.

# Algorithm
# Create a dictionary
# If sorted word not in dictionary,
#     # set words as key & index as value
# If sorted word in dictionary,
#     append index(value) for word

# [cat, dog, god, act, tac]

def anagram(A):
    if A == None:
        return
    else:
        dict = {}
        for i in range(len(A)):
            word = ' '.join(sorted(A[i])) # Sort in alphabetical order

            if word not in dict:
                dict[word] = [i+1] # dict[act] = [0+1] = [1]value, [2]value

            else: # [1,4].append(4+1) = [1,4,5]
                dict[word].append(i+1) # dict[dog].append(2+1)
        print(dict)

        # return dict
        # act:1,4,5; dog:2,3;

arr =  ["cat", "dog", "god", "act", "tac"]
print(anagram(arr)) # This will print the occurrence of word's indices