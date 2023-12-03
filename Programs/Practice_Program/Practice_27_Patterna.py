"""
1----------------1 column
1 2 1------------3 column
1 2 3 2 1--------5 column
1 2 3 4 3 2 1----6 column
Row = 4

i = 1,j = 1
i = 2, j = 1,2,3
i = 3, j = 1,2,3,4,5
i = 4, j = 1,2,3,4,5,6,7
"""

row = 4

column = 1
for i in range(1, row+1): # 1,2,3,4
    m = 0
    for j in range(1, column+1): # 1; 1to3; 1to5; 1to7;
        if j>i: # 1>1; 1>2,2>2,3>2; 1>3,2>3,3>3,4>3,5>3; 1>4,2>4,3>4,4>4,5>4,6>4,7>4;
            m = m-1
        else:
            m = m+1
        print(m,end=" ") # 1; 1,2,1; 1,2,3,2,1; 1,2,3,4,3,2,1;

    print()
    column = column+2


# column = 1
# for i in range(1, row + 1):
#     k=0
#     for j in range(1, column + 1):
#         if j > i:  # 3; 4,5; 5,6,7;
#             k = j-i  # 3-2=1; 4-3=1,5-3=2; 5-4=1,6-4=2,7-4=3
#             k = i-k  # 2-1=1; 3-1=2,3-2=1; 4-1=3,4-2=2,4-3=1;
#             print(k, end=" ")  # 1; 2,1; 3,2,1;
#
#         else:
#             print(j, end=" ")
#
#
#     print()
#     column = column + 2
