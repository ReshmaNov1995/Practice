"""
Find Missing number in an array

Input:
list1 = [1,2,3,5,6,7]

Output:
4
"""

def missing_num(list1):
    list2 = sorted(list1)
    # print(list2)
    size = len(list2)

    for i in range(size):
        if list2[i] != i+1: # 1!=0+1; 2!=1+1; 3!=2+1; 5!=3+1; 6!=4+1
            print(i+1)
            break


list1 = [1,2,7,5,4,3,6,9]
missing_num(list1)