# Full Number Pattern in increment/decrement order

n=5
for i in range(0,n+1):
    for j in range(1,i):
        print(str(j),end=" ")
    print()
for i in range(n+1,0,-1):
    for j in range(1,i):
        print(j,end=" ")
    print()
