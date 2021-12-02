import sys

if __name__ == "__main__":
	
	a = []
	with open(sys.argv[1], 'r') as fh:
		for val in fh.readlines():
			a.append(val.strip())

	h = 0
	d = 0
	aim = 0
	for instr in a:
		set = instr.split(' ')
		if set[0] == 'forward':
			h += int(set[1])
			d += int(set[1]) * aim
		elif set[0] == 'down':
			aim += int(set[1])
		elif set[0] == 'up':
			aim -= int(set[1])

	print(h*d)
