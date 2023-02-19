# https://adventofcode.com/2021/day/8 part 2
# Created by: Menaka S. 8 Dec 2021

import sys 
from collections import defaultdict

total = 0
digits = []

def split(word):
    return [char for char in word]

def present_in(word1, word2):
	w1 = split(word1)
	found = 1
	for i in range(0,len(w1)):
		if not w1[i] in word2:
			found = 0
	return found

for line in sys.stdin:
	mapping = dict()
	line = line.strip()
	(lhs,rhs) = line.split(' | ')

	#lhs
	digits = lhs.split()
	for i in range(len(digits)):
		digits[i] = "".join(sorted([char for char in digits[i]]))
	digits.sort(key=len)

	#rhs
	rdigits = rhs.split()
	for i in range(len(rdigits)):
		rdigits[i] = "".join(sorted([char for char in rdigits[i]]))

	mapping[1] = digits[0] #length 2
	mapping[7] = digits[1] #length 3
	mapping[4] = digits[2] #length 4
	mapping[8] = digits[9] #length 7

	# 0 6 9
	if not present_in(mapping[7],digits[6]):
		mapping[6] = digits[6]
		if present_in(mapping[4],digits[7]):
			mapping[9] = digits[7]
			mapping[0] = digits[8]
		if present_in(mapping[4],digits[8]):
			mapping[9] = digits[8]
			mapping[0] = digits[7]
	if not present_in(mapping[7],digits[7]):
		mapping[6] = digits[7]
		if present_in(mapping[4],digits[6]):
			mapping[9] = digits[6]
			mapping[0] = digits[8]
		if present_in(mapping[4],digits[8]):
			mapping[9] = digits[8]
			mapping[0] = digits[6]
	if not present_in(mapping[7],digits[8]):
		mapping[6] = digits[8]
		if present_in(mapping[4],digits[7]):
			mapping[9] = digits[7]
			mapping[0] = digits[6]
		if present_in(mapping[4],digits[6]):
			mapping[9] = digits[6]
			mapping[0] = digits[7]

	# 2 3 5
	if present_in(mapping[1],digits[3]):
		mapping[3] = digits[3]
		if present_in(digits[4],mapping[9]):
			mapping[5] = digits[4]
			mapping[2] = digits[5]
		if present_in(digits[5],mapping[9]):
			mapping[5] = digits[5]
			mapping[2] = digits[4]
	if present_in(mapping[1],digits[4]):
		mapping[3] = digits[4]
		if present_in(digits[3],mapping[9]):
			mapping[5] = digits[3]
			mapping[2] = digits[5]
		if present_in(digits[5],mapping[9]):
			mapping[5] = digits[5]
			mapping[2] = digits[3]
	if present_in(mapping[1],digits[5]):
		mapping[3] = digits[5]
		if present_in(digits[4],mapping[9]):
			mapping[5] = digits[4]
			mapping[2] = digits[3]
		if present_in(digits[3],mapping[9]):
			mapping[5] = digits[3]
			mapping[2] = digits[4]


	inv_map = {v: k for k, v in mapping.items()}
	num = 0
	ct = 3
	for d in rdigits:
		num += int(inv_map[d]) * (10** ct)
		ct -=1

	total += num
print(total)

