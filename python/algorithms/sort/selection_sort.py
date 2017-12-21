'''
Time complexility: O(n^2)
(n - 1) + (n - 2) + (n - 3) + ... + 1 = n*(n-1)/2
'''
def ssort(k):
    for i in range(0, len(k) - 1):
        for j in range(i+1, len(k)):
            if(k[i] > k[j]):
                temp = k[j]
                k[j] = k[i]
                k[i] = temp

k = [1, 3, 4, 10, 5, 4]

ssort(k)

assert(k == [1, 3, 4, 4, 5, 10])
