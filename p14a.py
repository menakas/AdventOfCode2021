# https://adventofcode.com/2021/day/14 part 1
# Created by: Menaka S. 14 Dec 2021

import sys 
import re

rules = {}
template = ''
temp = 1

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

step = 0
mx = 10
while step < mx:
	newtemplate = ''
	prev = template[0]
	for i in range(1,len(template)):
		newtemplate = newtemplate + prev
		key = template[i-1:i+1]
		if rules[key]:
			newtemplate = newtemplate + rules[key]
		prev = template[i:i+1]
	newtemplate = newtemplate + prev
	template = newtemplate	
			
	step +=1
	#print("Step",step,":",template,len(template))

counts = {}
for i in range(65,91):
	n = template.count(chr(i))
	if n:
		counts[chr(i)] = n
	
#print(counts)

print(max(counts.values()) - min(counts.values()))

	

