# https://adventofcode.com/2021/day/10 part 2
# Created by: Menaka S. 10 Dec 2021

import sys 

lines = []

def split(word):
    return [char for char in word]

for line in sys.stdin:
	lines.append(split(line.strip()))

opens = dict();
opens['('] = ')'
opens['['] = ']'
opens['{'] = '}'
opens['<'] = '>'

points = dict()
points[')'] = 1
points[']'] = 2
points['}'] = 3
points['>'] = 4

scores = []

for line in lines:
	stack =  []
	compscore = 0
	error = 0
	for j in range(len(line)):
		if line[j] in opens:
			stack.append(line[j]) 
		if line[j] in opens.values():
			exp = stack.pop()
			if opens[exp] != line[j]:
				error = 1
	if not error and len(stack) > 1:
		for j in range(len(stack)-1,-1,-1):
			compscore = (compscore * 5 ) + points[opens[(stack[j])]]
		scores.append(compscore)
		#print(stack,compscore)

scores.sort()
#print(scores)
print(scores[int(len(scores)/2)])
