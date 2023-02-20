# https://adventofcode.com/2021/day/25
# Created by: Menaka S. 25 Dec 2021

import sys
import copy

lines = []
def split(word):
	return [char for char in word]

for line in sys.stdin:
	line = line.strip()
	lines.append(split(line))

step = 0

moved = 1000
newlines = copy.deepcopy(lines)
while moved:
	moved = 0
	movedpos = dict()
	for i in range(len(lines)):
		for j in range(len(lines[i])):
			if j == len(lines[i]) - 1:
				nextj = 0
			else:
				nextj = j+1
			if lines[i][j] == '>' and lines[i][nextj] == '.':
					#print(i,j,nextj)
					newlines[i][nextj] = '>'
					movedpos[(i,nextj)] = 1
					newlines[i][j] = '.'
					moved+=1
			elif (i,j) not in movedpos.keys():
					#print(i,j,"overwri?")
					newlines[i][j] = lines[i][j]
			#print(movedpos)
		
	movedpos = dict()
	for i in range(len(newlines)):
		for j in range(len(newlines[i])):
			if i == len(newlines) - 1:
				nexti = 0
			else:
				nexti = i+1
			if newlines[i][j] == 'v' and newlines[nexti][j] == '.':
					lines[nexti][j] = 'v'
					movedpos[(nexti,j)] = 1
					lines[i][j] = '.'
					moved+=1
			elif (i,j) not in movedpos.keys():
					lines[i][j] = newlines[i][j]
	step += 1
print(step)
