# Find Substring

# Conserve sequence
# Don't skip any character in between
# Vary from 1 character of string to length of the string

def substring(str1, n): # n=5
    for i in range(n): # 0 to 4
        for j in range(i+1, n+1): # 0+1=1, 5+1=6(5)
            print(str1[i:j]) # 0,1; 0,2;.....

str1 = "TANUJ"
n = len(str1)
substring(str1, n)

