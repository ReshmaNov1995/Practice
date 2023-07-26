# Method - 1: Rotation of String

name = 'Reshma'

size = len(name)
list1 = list(name)
for i in range(size):

    list1.pop(0)
    list1.append(name[i])
    print(''.join(list1))



# # Method - 2: Rotation of String
#
# name = 'Reshma'
#
#
# lista = list(name)
# size = len(lista)
#
# for i in range(size-1):
#     temp = lista[0]
#     lista.pop(0)
#     lista.append(temp)
#     print(''.join(lista))