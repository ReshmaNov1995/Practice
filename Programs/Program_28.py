# Pattern in incremental order

n=5

for i in range(1,n+1): # 1;2;3;4;5
    for j in range(1,i+1): # 1; 1to2; 1to3; 1to4; 1to5.
        print(j,end=" ") # 1; 1 2; 1 2 3; 1 2 3 4; 1 2 3 4 5
    print()