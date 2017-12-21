'''
Time complexility
Best: O(nlgn)
Bad: O(n^2)
Avarage: O(nlgn)
'''
def qsort(k, l, h):

    if l >= h:
        return

    pivot = k[int( (l+h) /2 )]
    i = l
    j = h

    while True:
        while k[i] < pivot:
            i += 1

        while k[j] > pivot:
            j -= 1

        if i <= j:
            if i < j:
                temp = k[i]
                k[i] = k[j]
                k[j] = temp
            i += 1
            j -= 1

        if i > j:
            break

    qsort(k, l, j)
    qsort(k, i, h)

k = [1, 3, 4, 10, 5, 4]

'''
pivot = 4
i = 2 k[i]=4
j = 5 k[j]=4

i=3 ->10
j=4 ->5

qsork(k, 0,3)
qsort(k, 4, 5)
'''

qsort(k, 0, len(k) - 1)

assert(k == [1, 3, 4, 4, 5, 10])
