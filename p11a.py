# https://adventofcode.com/2021/day/11 part 1
# Created by: Menaka S. 11 Dec 2021

import sys 

lines = []

def split(word):
	return [int(char) for char in word]

def increment(i,j):
	if i >= 0 and i < len(lines[0]) and j >= 0 and j < len(lines[0]):
		lines[i][j] += 1
		if lines[i][j] > 9 and (i,j) not in flashed:
			toflash.add((i,j))
		return 1
	return 0

def flash(i,j):
	#print("Flashing..",i,j)
	flashed.add((i,j))
	increment(i+1,j-1)
	increment(i+1,j)
	increment(i+1,j+1)
	increment(i,j-1)
	increment(i,j+1)
	increment(i-1,j-1)
	increment(i-1,j)
	increment(i-1,j+1)


for line in sys.stdin:
	lines.append(split(line.strip()))

step = 0
mx = 100
flashes = 0
while step < mx:
	toflash = set()
	flashed = set()
	for i in range(len(lines[0])):
		for j in range(len(lines[0])):
			lines[i][j] +=1
			if(lines[i][j] > 9):
				toflash.add((i,j))
	while len(toflash) > 0:
		(i,j) = toflash.pop()
		flash(i,j)
	for (x,y) in flashed:
		if lines[x][y] > 9:
			lines[x][y] = 0
			flashes += 1

	step +=1
print(flashes)

