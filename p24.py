# https://adventofcode.com/2021/day/24
# Created by: Menaka S. 24 Dec 2021

import sys 

digits = dict()
stack = list()

with sys.stdin as f:
	dig = 0
	for i, line in enumerate(f):
		_, *operands = line.rstrip().split(' ')
		if i % 18 == 4: push = operands[1] == '1'
		if i % 18 == 5: sub = int(operands[1])
		if i % 18 == 15:
			if push:
				#print(dig, " if")
				stack.append((dig, int(operands[1])))
				#print(stack)
			else:
				#print(dig, " inelse", sub)
				sibling, add = stack.pop()
				diff = add + sub
				if diff < 0:
					digits[sibling] = (-diff + 1, 9)
					digits[dig] = (1, 9 + diff)
				else:
					digits[sibling] = (1, 9 - diff)
					digits[dig] = (1 + diff, 9)
				#print(digits)
			dig += 1

print(''.join(str(digits[d][1]) for d in sorted(digits.keys())))
print(''.join(str(digits[d][0]) for d in sorted(digits.keys())))

