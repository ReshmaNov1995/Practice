# String is Palindrome or Not

# function which return reverse of a string

string=input(("Enter a letter:"))

if(string==string[::-1]):
      print("The letter is a palindrome")
else:
      print("The letter is not a palindrome")

# Palindrome number program using while loop

num = 1221
temp = num
reverse = 0
while temp > 0:
    remainder = temp % 10
    reverse = (reverse * 10) + remainder
    temp = temp // 10
if num == reverse:
  print('Palindrome')
else:
  print("Not Palindrome")