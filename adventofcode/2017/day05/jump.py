# part 1
def run(f):
	ints = []
	with open(f, 'r') as input:
		for line in input:
			ints.append(int(line))
	
	step = 0
	cur = 0
	while cur < len(ints) or cur < 0:
		step += 1
		pre = cur
		cur = cur + ints[cur]
		ints[pre] += 1
	
	return step


assert (run('test') == 5)
print(run('input'))  # 374269


# part 2
def run(f):
	ints = []
	with open(f, 'r') as input:
		for line in input:
			ints.append(int(line))
	
	step = 0
	cur = 0
	while cur < len(ints) or cur < 0:
		step += 1
		pre = cur
		cur = cur + ints[cur]
		if ints[pre] >= 3:
			ints[pre] -= 1
		else:
			ints[pre] += 1
	
	return step


assert (run('test') == 10)
print(run('input'))  # 27720699
