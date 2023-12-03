"""
Input:
string = "Reshma is a new QA Lead, Welcome to the Organisation Reshma."

Output:
{Reshma:2, is:1, a:1, new:1, QA:1, Lead:1}
"""

def freq_words(string):
    listconv = string.split()
    size = len(listconv)
    dict = {}

    for i in range(size):
        if ',' in listconv[i]:
            strip = listconv[i].strip(',')

            if strip not in dict:
                dict[strip] = 1

            else:
                dict[strip] = dict[strip] + 1

        if '.' in listconv[i]:
            strip1 = listconv[i].strip('.')

            if strip1 not in dict:
                dict[strip1] = 1

            else:
                dict[strip1] = dict[strip1] + 1

        else:
            if listconv[i] not in dict:
                dict[listconv[i]] = 1

            else:
                dict[listconv[i]] = dict[listconv[i]] + 1
    print(dict)

string = "Reshma is a new QA Lead, Welcome to the Organisation Reshma."

freq_words(string)