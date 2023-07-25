# Remove duplicate from sorted array

def remove_dup(arr):
    n = len(arr)
    list_a = list()
    for i in range(n-1):
        if arr[i] != arr[i+1]:
            list_a.append(arr[i])
    list_a.append(arr[-1]) # last Element
    print(list_a)

arr = [1,1,2,3,4,4,4,5,5]
remove_dup(arr)