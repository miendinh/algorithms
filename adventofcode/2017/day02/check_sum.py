# part 1
def caculate(f):
	with open(f, 'r') as input:
		sum = 0
		for line in input:
			rows = [int(x) for x in line.split('\t')]
			sum += max(rows) - min(rows)
		
		return sum


assert (caculate('test') == 18)

print(caculate('input'))


# part 2
def caculate(f):
	with open(f, 'r') as input:
		sum = 0
		for line in input:
			rows = [int(x) for x in line.split('\t')]
			for i in range(len(rows)):
				for j in range(len(rows)):
					if i <= j:
						continue;
					
					low, heigh = (rows[i], rows[j]) if rows[i] < rows[j] else (rows[j], rows[i])
					if heigh % low == 0:
						print(low, ' ', heigh, ' ', heigh % low)
						sum += heigh / low
		print(sum)
		return int(sum)


assert (caculate('test2') == 9)
print(caculate('input'))
