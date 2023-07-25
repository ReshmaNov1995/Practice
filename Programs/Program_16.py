# First Non Repeating character in a string with the Index value

# Dictionary -> Key & Value. Here Key is a list's index value and value is a list index value's occurrence

def first_non_repeating(str_r):
    dict = {}
    size = len(str_r)

    for i in range(size):
        key = str_r[i]
        if key not in dict:
            dict[key] = 1

        else:
            dict[key] = dict[key] + 1
    print(dict)

# Non repeating character with index position
    counter = 0
    for i in range(size):
        if dict[str_r[i]] == 1: # dict[str_r[i]] -> dict[str_r[0]] -> dict["N"] -> count of occurrence of "N" ->
            # print(dict[str_r[index]])
            return str_r[i], counter
        counter = counter+1

# # Non repeating character with occurrence
#     print(dict)
#
#     for key,value in dict.items():
#         if value == 1:
#             print(key, value)
#             break

str_r = "NETSETOSNETM"
print(first_non_repeating(str_r))