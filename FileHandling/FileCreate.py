import os

filepath="D:\\sample\\tst.txt"
result=os.path.isfile(filepath)

if result==True:
    print("File Exist")
else:
    txt=open(filepath,"w")
    print("File Created")
