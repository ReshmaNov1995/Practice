"""
a = [7, 4, 8, 2] in ascending
order
"""

def method(a):
    # b = []
    size = len(a)

    for i in range(size):
        for j in range(size):
            if a[i] <= a[j]:
                a[i], a[j] = a[j], a[i]
    print(a)

a = [7, 4, 8, 2]
method(a)