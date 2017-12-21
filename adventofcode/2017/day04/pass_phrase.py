# part 1
def check(str):
	arr = str.split(' ')
	for i in range(len(arr) - 1):
		for j in range(i + 1, len(arr)):
			if arr[i].strip() == arr[j].strip():
				return False
	
	return True


def count(f):
	count = 0
	with open(f, 'r') as input:
		for line in input:
			if check(line):
				count += 1
	
	return count


assert (check('aa bb cc dd ee') == True)
assert (check('aa bb cc dd aa') == False)
assert (check('aa bb cc dd aaa') == True)
assert (count('test') == 2)

print(count('input'))  # 451


# part 2
def check(str):
	arr = [x.strip() for x in str.split(' ')]
	for i in range(len(arr) - 1):
		for j in range(i + 1, len(arr)):
			if sorted(arr[i]) == sorted(arr[j]):
				return False
	
	return True


def count(f):
	count = 0
	with open(f, 'r') as input:
		for line in input:
			if check(line):
				count += 1
	
	return count


assert (check('abcde fghij') == True)
assert (check('abcde xyz ecdab') == False)
assert (check('a ab abc abd abf abj') == True)
assert (check('iiii oiii ooii oooi oooo') == True)
assert (check('oiii ioii iioi iiio') == False)
assert (count('test2') == 3)

print(count('input'))  # 223
