# # Example 1: String can be stored as,
#
# a = "resh"
# a = 'resh'
# a = str("resh")
# a = str('resh')
#
# # Empty String variables
#
# a = ""
# a = ''
# a = str("")
# a = str()
#
# # Example 2: String is immutable.
#
# x = "Hi" # String will allocate the memory for the variable.
# print(id(x)) # It 'll give the id of the memory location. 1567909627056
#
# x = "Hello"
# print(id(x)) # 1567909627120
#
# # Example 3: + and * with String
#
# # + concatenation
# i = "Hi"
# print(i+" Python")
#
# # * String value multiple times
# print(i*7)
#
# # Example 4: Slicing [] - while slice it should start from, 1 for ending index and 0 for starting index.
#
# str = "Welcome to Automation"
# print(str[2:5])
#
# print(str[:7]) # Default starting index is 0
# print(str[2:]) # It ll print all the values followed by starting index
# print(str[1:-1]) # End index ll neglect from the last value for negative integers
#
# # Example 5: ord() and chr()
#
# # ord() for character to ASCII value
# print(ord("Z"))
# # chr() for ASCII value to character
# print(chr(70))
#
# # Example 6: max() min() len()
#
# print(max("drshxusz"))
# print(min("bhdgcdshcjdsbgvhja"))
# print(len("dhcfsfghuesdjhxvdebxjk"))
#
# # Example 7: in, not in - returns True/False
#
# f = "Am a Robot"
#
# print("Am" in f)
# print("Am" not in f)
#
# print("Reshu" in f)
# print("Reshu" not in f)
#
# # Example 8: String Comparison by relational operator
# # Comparison done between the greater alphabets
#
# print("trim" == "trum")
# print("free" != "freedom")
# print("Table" > "Chair")
# print("trimble" < "trim")
# print("right" >= "left")
# print("yellow" <= "fellow")
# print("abc" > "")

# Example 9: Testing Strings

s = "Welcome to Learn Automation Online"
a = "earnAutoma"
print(s.isalnum()) # check for alpha or numeric. Space is not under alphanumeric.
print(a.isalnum())
print("welcome".isalpha()) # check for only alphabet
print("2012".isdigit()) # check for only digit

print("first number".isidentifier())  # A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_).
# A valid identifier cannot start with a number, or contain any spaces.

print(s.islower()) # check for lowercase
print("WELCOME".isupper()) # check for uppercase
print(" ".isspace()) # check for space

# Example 10:
