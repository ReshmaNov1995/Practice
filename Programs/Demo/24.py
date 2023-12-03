"""
Palindrome String, Number

Input:
"Malyalam"

Output:
"Malyalam" is a palindrome
"""

# def pal_string():
#     str = input()
#     rev = str[::-1]
#     if rev == str:
#         print(str, "is a palindrome")
#     else:
#         print("Not a palindrome")
#
# pal_string()


def pal_num():
    num = int(input())
    rev = 0
    temp = num

    while temp != 0:
        digit = temp % 10
        rev = (rev * 10) + digit
        temp = temp // 10

    print(rev)

    if rev == num:
        print(num, " is a palindrome")

    else:
        print("Not a palindrome")

pal_num()
