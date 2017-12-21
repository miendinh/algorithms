def bsort(k):
    for i in range(0, len(k)):
        for j in range(len(k)-1, i, -1):
            if k[j] > k[j-1]:
                temp = k[j]
                k[j-1] = k[j]
                k[j] = temp

k = [1, 3, 4, 10, 5, 4]

bsort(k)

print(k)

assert(k == [1, 3, 4, 4, 5, 10])
