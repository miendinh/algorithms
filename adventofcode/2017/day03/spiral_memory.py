input = 361527

'''
17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...
'''

'''
(-2,2)    (-1,2)      (0,2)   (1,2)   (2,2)

(-2,1)    (-1,1)      (0,1)   (1,1)   (2,1)

(-2,0)    (-1,0)      (0,0)   (1,0)   (2,0)

(-2,-1)    (-1,-1)    (0,-1)  (1,-1)  (2,-1)

(-2,-2)    (-1,-2)    (0,-2)  (1,-2)  (2,-2)

'''


def move(n):


# TODO



assert (move(1) == 0)
assert (move(12) == 3)
assert (move(23) == 2)
assert (move(1024) == 31)

print(move(input))
