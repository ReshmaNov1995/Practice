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

def substring(str):
    size = len(str)

    for i in range(size):
        for j in range(i+1, size+1):
            substr = str[i:j]
            print(substr)

str = "karun"

substring(str)