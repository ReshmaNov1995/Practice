"""
Palindrome String, Number

Input:
"Malyalam"

Output:
"Malyalam" is a palindrome
"""

# def palindrome(str):
#     str = input("Enter a text:")
#     rev = str[::-1]
#
#     if str == rev:
#         print("Given String is palindrome", rev)
#
#     else:
#         print("Given String " +str+ " is not a palindrome", rev)
#
# palindrome(str)


def palindrome_num():

    num = int(input()) # 121
    rev = 0
    temp = num
    while temp != 0: # 121, 12, 1
        digit = temp%10 # display only last digit 1; 2; 1
        rev = (rev*10) + digit # 1; 12; 121
        temp = temp//10 # display num except last digit 12(121/10=12.1; Roundoff = 12); 12.1(12); 1.2(1); 0.1(0)
    print(rev)

    if num == rev:
        print("palindrome")

    else:
        print("Not a palindrome")

palindrome_num()

