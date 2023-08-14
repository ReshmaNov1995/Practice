# Pattern in incremental order

"""
1 --------------- 1 column
1 2 --------------2
1 2 3 ------------3
1 2 3 4 ----------4
1 2 3 4 5 --------5
Row = 5
"""

n=5

# for i in range(1,n+1): # 1;2;3;4;5
#     for j in range(1,i+1): # 1; 1to2; 1to3; 1to4; 1to5.
#         print(j,end=" ") # 1; 1 2; 1 2 3; 1 2 3 4; 1 2 3 4 5
#     print()

column = 1
column_value = 1
for i in range(1,n+1): # 1;2;3;4;5
    for j in range(1,column+1): # 1; 1to2; 1to3; 1to4; 1to5.
        print(column_value,end=" ") # 1; 1 2; 1 2 3; 1 2 3 4; 1 2 3 4 5
        column_value = column_value + 1

    print()
    column = column + 1