# part 1 & part 2
def find_max(banks):
	max_block = max(banks)
	max_index = None
	
	for i in range(len(banks)):
		if (banks[i] == max_block):
			max_index = i
			break
	
	return (max_index, max_block)


def distribute(banks):
	max_index, max_block = find_max(banks)
	amount = banks[max_index] // (len(banks) - 1)
	amount = amount if amount > 0 else 1
	next_bank = (max_index + 1) % len(banks)
	while banks[max_index] >= amount and next_bank != max_index:
		banks[next_bank] += amount
		banks[max_index] -= amount
		next_bank = (next_bank + 1) % len(banks)
	
	return banks


def relocation(f):
	banks = []
	with open(f, 'r') as input:
		for line in input:
			banks = [int(x) for x in line.split('\t')]
			break;
	
	config = []
	seen_at = []
	pattern = None
	no_cycle = 0
	
	while pattern not in config:
		if pattern:
			config += [pattern]
			seen_at += [no_cycle]
		
		banks = distribute(banks)
		no_cycle += 1
		pattern = [' '.join(str(b) for b in banks)][0]
	
	idx = next(i for i in range(len(config)) if config[i] == pattern)
	
	no_dist = no_cycle - seen_at[idx]
	
	return (no_cycle, no_dist)


assert (relocation('test')[0] == 5)
print(relocation('input'))  # (14029, 2765)
