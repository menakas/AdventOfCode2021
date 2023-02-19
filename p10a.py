# https://adventofcode.com/2021/day/10 part 1
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
points[')'] = 3
points[']'] = 57
points['}'] = 1197
points['>'] = 25137

errorscore = 0

for line in lines:
	stack =  []
	for j in range(len(line)):
		if line[j] in opens:
			stack.append(line[j]) 
		if line[j] in opens.values():
			exp = stack.pop()
			if opens[exp] != line[j]:
				#print('Expected ',opens[exp],'but found',line[j])
				errorscore += points[line[j]]

print(errorscore)
