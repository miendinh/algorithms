# part 1 & part 2
import re

class P:
	def __init__(self, name, val = 0):
		self.name = name
		self.val = val
		self.next = None
		self.towers = []

	def set_next(self, next_):
		self.next = next_

	def get_next(self):
		return set.next

	def set_name(self, name):
		self.name = name

	def set_val(self, val):
		self.val = val

	def add_tower(self, tower):
		self.towers.append(tower)

def get_attr(line):
	towers = []
	if '->' in line:
		m = re.search('([a-z]+)\s\((\d+)\)\s\-\>\s([a-z,\s]+)', line)
		towers = m.group(3)
		towers = [ t.strip() for t in towers.split(',') ]
	else:
		m = re.search('([a-z]+)\s\((\d+)\)', line)

	name = m.group(1)
	weight = m.group(2)

	return (name, weight, towers)

def build(f):
	programs = []
	with open(f, 'r') as input:
		for line in input:
			name, weight, towers = get_attr(line)
			p = P(name, weight)
			programs.append(p)

			if len(towers) > 1:
				for t in range(1, len(towers)):
					p.add_tower(t)

	return programs

def find_bottom(f):
	programs = build(f)
	bottom = None
	count = 0
	for p in programs:
		while p.get_next():


build('test')
