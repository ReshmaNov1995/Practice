# Find common letters b/w 2 strings
# Ex: Naina, Reene

def common_letters():
    str1 = input("Enter First String: ")
    str2 = input("Enter Second String: ")
    # To remove duplicate use Set
    s1 = set(str1)
    s2 = set(str2)
    # print(s1, s2)
    string = s1 & s2 # And operator will fetch the common matching b/w 2 strings
    print(string)

common_letters()