"""
1 --------------- 1 column
1 2 --------------2
1 2 3 ------------3
1 2 3 4 ----------4
1 2 3 4 5 --------5
Row = 5
"""

# row = 5
# column = 1
# for i in range(1, row+1):
#     for j in range(1, column+1):
#         print(j, end=" ")
#
#     print()
#     column = column+1

"""
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
"""

# row = 5
# column = 1
# column_value = 1
# for i in range(1, row+1):
#     for j in range(1, column+1):
#         print(column_value, end=" ")
#         column_value = column_value+1
#
#     print()
#     column = column+1


"""
    1 --------------- 1 column 4 space
   1 2 --------------2   3 space
  1 2 3 ------------3    2 space
 1 2 3 4 ----------4     1 space
1 2 3 4 5 --------5      0 space
Row = 5
"""

# row = 5
# column = 1
# space = 4
# for i in range(1, row+1):
#     for k in range(1, space+1):
#         print("", end=" ")
#     for j in range(1, column+1):
#         print(j, end=" ")
#
#     print()
#     space = space-1
#     column = column+1

"""
1 2 3 4 5---5 col
1 2 3 4-----4
1 2 3-------3
1 2---------2
1-----------1
Row = 5
"""

# row = 5
# column = 5
# for i in range(1, row+1):
#     for j in range(1, column+1):
#         print(j, end=" ")
#
#     print()
#     column = column-1


"""
1 2 3 4 5---5 col  0 space
 1 2 3 4-----4     1 space
  1 2 3-------3    2 space
   1 2---------2   3 space
    1-----------1  4 space
Row = 5
"""

row = 5
column = 5
space = 0
for i in range(1, row+1):
    for k in range(1, space+1):
        print("", end=" ")
    for j in range(1, column+1):
        print(j, end=" ")

    print()
    space = space+1
    column = column-1