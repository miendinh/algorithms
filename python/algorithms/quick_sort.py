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

qsort(k, 0, 5)

assert(k == [1, 3, 4, 4, 5, 10])
