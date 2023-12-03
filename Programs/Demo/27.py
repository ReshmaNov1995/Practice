"""
1----------------1 column
1 2 1------------3 column
1 2 3 2 1--------5 column
1 2 3 4 3 2 1----6 column
Row = 4
"""

row = 4
column = 1
for i in range(1, row+1):
    m = 0
    for j in range(1, column+1):
        if j>i:
            m = m-1
        else:
            m = m+1
        print(m, end=" ")

    print()
    column = column+2