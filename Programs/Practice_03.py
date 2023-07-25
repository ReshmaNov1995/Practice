"""
Input:
create tuple = ('user01', [checkbox1, checkbox2], [radiobutton1, radiobutton2], save1)

Output:
print(tuple1[0], "is logged in")
print((tuple1[1])[0], "is clicked")
print((tuple1[1])[1], "is clicked")
print((tuple1[2])[0], "is clicked")
print((tuple1[2])[1], "is clicked")
print(tuple1[3], "is Saved")
"""

def tup_list(tuple1):
    size = len(tuple1)
    List = []

    for i in range(size):
        if i == 0:
            print(tuple1[i], "is logged in")

        if type(tuple1[i]) == type(List):
            for j in range(len(tuple1[i])):
                print((tuple1[i])[j], "is clicked")

        if i == size-1:
            print(tuple1[i], "is saved")



tuple1 = ('user01', ['checkbox1', 'checkbox2'], ['radiobutton1', 'radiobutton2'], 'save1')
tup_list(tuple1)


