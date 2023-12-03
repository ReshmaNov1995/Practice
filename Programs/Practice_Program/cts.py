str1 = 'RE123k'
for i in str1:
    try:
        print(int(i))
    except Exception as E:
        print("It is a string character",i)


