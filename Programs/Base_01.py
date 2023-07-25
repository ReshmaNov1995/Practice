# 1:[0,5], 2:[1,6], 3:[2], 4:[3], 5:[4]



list = [1,2,3,4,5,1,2]
dict = {}

for i in range(len(list)):
    if list[i] not in dict:
        dict[list[i]] = [i]

    else:
        dict[list[i]].append(i)

print(dict)






