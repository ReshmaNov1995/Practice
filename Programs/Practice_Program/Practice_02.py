"""
Count the Frequency of words appearing in a String

Input:
Hello Reshma and Hello Roja

Output:
Hello:2, Reshma:1, and:1, Roja:1
"""

def frequencyofword(string):
    str = string.split()

    size = len(str)
    dict = {}

    for i in range(size):
        if str[i] not in dict:
            dict[str[i]] = 1

        else:
            dict[str[i]] = dict[str[i]] + 1

    print(dict)

string = "Hello Reshma and Hello Roja"
frequencyofword(string)