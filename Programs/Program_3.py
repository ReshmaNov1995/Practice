# Convert 2 lists into dictionary

def list_to_dict():
    key = ['Naina', 'Kimi', 'Sheena']
    value = [852345, 763567, 691276]
    result = dict(zip(key, value)) # zip will map the keys to values
    print(result)


list_to_dict()

# Convert dictinary to tuples

def dict_to_tuple():
    a = tuple()
    x = {'Naina': 852345, 'Kimi': 763567, 'Sheena': 691276}
    for i in x.items(): # items method will convert dictionary into tuple. If u use i,j then it will fetch the same as normal data.
        # print(i)
        a = a+i
    print(a)
dict_to_tuple()