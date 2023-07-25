# Reverse words in a sentence

def reverse(str_r):
    str_r = str_r[::-1]
    return str_r

# print(reverse("Reshma"))

def reverse_words(str_r):
    n = len(str_r)
    if n == 1:
        return str_r

    str2 = str_r.split(" ") # Spaces will be removed and give as single word
    size = len(str2)
    rev_all = ""

    for i in range(size):
        rev = reverse(str2[i])
        print(rev)
        rev_all = rev_all + rev + " "
    # print(rev_all)
    d = reverse(rev_all)
    return d.strip() # Unwanted Spaces will be removed from the starting(leading) and ending(trailing)

str_e =  "NETSETOS is learning platform"
print(reverse_words(str_e))