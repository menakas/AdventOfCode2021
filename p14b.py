# https://adventofcode.com/2021/day/14 part 2
# Created by: Menaka S. 14 Dec 2021

import sys 
import copy 
import re

rules = {}
template = ''
temp = 1
counts = {}
ccounts = {}

for line in sys.stdin:
	line = line.strip()
	if line == '':
		continue
	if temp:
		template = line
		temp = 0
	else:
		(lhs,rhs) = line.split(' -> ')
		rules[lhs] = rhs


for i in range(0,len(template)-1):
	counts[template[i]+template[i+1]] = 1

step = 0
mx = 40
while step < mx:
	newcounts = {}
	for item in counts:
		if rules[item]:
			lhs = item[0]+rules[item]
			rhs = rules[item] + item[-1]
			if lhs not in newcounts:
				newcounts[lhs] = 0
			if rhs not in newcounts:
				newcounts[rhs] = 0
			if lhs in newcounts:
				newcounts[lhs] += counts[item]
			else:
				newcounts[lhs] = counts[item]
			if rhs in newcounts:
				newcounts[rhs] += counts[item]
			else:
				newcounts[rhs] = counts[item]
			
	counts = copy.deepcopy(newcounts)
	step +=1
	#print("Step", step, counts)

#print(counts)
for item in counts:
	if item[0] not in ccounts:
		ccounts[item[0]] = counts[item]
	else:
		ccounts[item[0]] += counts[item]

ccounts[template[-1]] += 1

#print(ccounts)

print(max(ccounts.values()) - min(ccounts.values()))

	

