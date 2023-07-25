"""
Input:
string = "Reshma is a new QA Lead, Welcome to the Organisation Reshma."

Output:
{Reshma:2, is:1, a:1, new:1, QA:1, Lead:1}
"""

def occurrence_dict(string):
    list_str = string.split()
    # print(list_str)

    size = len(list_str)

    dict = {}
    for i in range(size):
        if ',' in list_str[i]:
            strip = list_str[i].strip(',')

            if strip not in dict:
                dict[strip] = 1

            else:
                dict[strip] = dict[strip]+1


        elif '.' in list_str[i]:
            strip1 = list_str[i].strip('.')

            if strip1 not in dict:
                dict[strip1] = 1

            else:
                dict[strip1] = dict[strip1]+1

        else:
            if list_str[i] not in dict:
                dict[list_str[i]] = 1

            else:
                dict[list_str[i]] = dict[list_str[i]]+1



    print(dict)



string = "Reshma is a new QA Lead, Welcome to the Organisation Reshma."
occurrence_dict(string)