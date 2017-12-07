# part 1
def crack(str):
    sum = 0;
    for c in range(len(str) - 1):
        if (str[c] == str[c+1]):
            sum = sum + int(str[c])

    return  (sum + int(str[0])) if (str[0] == str[-1]) else sum


assert( crack('1122') == 3 )
assert( crack('1111') == 4 )
assert( crack('1234') == 0 )
assert( crack('91212129') == 9 )

with open('input', 'r') as input:
    for line in input:
        print(crack(line.strip()))

#part 2
def crack(str):
    sum = 0;
    lenght = len(str)
    for c in range(lenght):
        next_step = (c + int(lenght/2)) % lenght
        if (str[c] == str[next_step]):
            sum = sum + int(str[c])

    return sum

assert( crack('1212') == 6 )
assert( crack('1221') == 0 )
assert( crack('123425') == 4 )
assert( crack('123123') == 12 )
assert( crack('12131415') == 4 )

with open('input', 'r') as input:
    for line in input:
        print(crack(line.strip()))
