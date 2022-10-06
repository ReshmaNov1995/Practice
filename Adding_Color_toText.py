# Method - 1:

# from termcolor import colored
#
# # colored function
# # syntax : colored(text, color, attribute_array)
# text = colored("Am Reshma", "red", attrs=["reverse", "blink"])
# print(text)

# Method - 2: This method is Approachable

from colorama import Fore, Back, Style

# syntax: Fore.(color_of_text, text)

print(Fore.RED,"Am Reshma")  #Foreground
print(Back.BLACK, "Am Reshma") #Background
print(Style.BRIGHT, "Am Roja") #Style
print(Style.RESET_ALL, "Am Reshma")