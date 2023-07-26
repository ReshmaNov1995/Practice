"""
Substring

Input:
karun

Output:
k
ka
kar
karu
karun
a
ar
aru
arun
r
ru
run
u
un
n
"""


name = "Karun"

size = len(name)
for i in range(size):
    for j in range(i+1, size+1): # 1,2,3,4,5
        substring = name[i:j] # 0:1; 0:2; 0:3; 0:4; 0:5.
        print(substring)

