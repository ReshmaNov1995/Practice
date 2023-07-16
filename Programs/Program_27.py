# Basic number pattern

# n=5
# sum=0
# for i in range(n,0,-1): # 5,4,3,2,1
#     sum=sum+1 # 2 3 4 5
#     for j in range(1,i+1): # 1,2,3,4,5
#         print(sum,end=" ") # 11111; 2222; 333; 44; 5
#     print('')

# Reverse Basic number pattern
n=5
sum=0
for i in range(1, n+1): # 1,2,3,4,5
    sum=sum+1 # 2 3 4 5
    for j in range(1,i+1): # 1,2,3,4,5
        print(sum,end=" ") # 11111; 2222; 333; 44; 5
    print('')