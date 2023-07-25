# Length of Last word

def length_lastword(A):
    arr = A.split()
    size = len(arr)

    if size == 1: # If input has only 1 word
        return len(A)

    last_word = arr[-1]
    print(len(last_word))

A = "Hello Reshma"
length_lastword(A)