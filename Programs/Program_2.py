# Count the Frequency of words appearing in a String

# String: Sheela loves eating apple and mango. Her sister also loves eating apple and mango.

# Method -1:

def freq_words():
    str = input("Enter the String: ") # key
    splt = str.split()
    print(splt)
    d = {}

    for i in splt:
        if i not in d.keys():
            d[i] = 0 # Sheela : 0
        d[i] = d[i]+1 # Sheela : 0+1 -> Sheela : 1
    print(d)

# Method - 2: Ignore
#
# def freq_words1():
#     str = input("Enter the String: ")
#     splt = str.split()
#     d = {}
#
#     for i in splt:
#         d[i] = d.get(i,0) + 1
#     print(d)

freq_words()
