# Finding duplicate Characters in a string

#using list
string = input()
dups=[]
for ch in string:
  if string.count(ch)>1 and ch not in dups:
    dups.append(ch)
print('The duplicate characters are {}'.format(dups))