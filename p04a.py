# https://adventofcode.com/2021/day/4 part 1
# Created by: Menaka S. 4 Dec 2021

import sys 

nums = []
first = 0
none = 0
ctr = -1
matrix = []


def calculatescore(ctr):
	total = 0
	for i in range(0,5):
		for j in range(0,5):
				total += int(matrix[ctr][i][j])
	return total

def hascomplete(ctr):
	#rows
	for i in range(0,5):
		marked = 1
		for j in range(0,5):
			if matrix[ctr][i][j] != '0':
				marked = 0
		if marked == 1:
			return 1

	#columns
	for i in range(0,5):
		marked = 1
		for j in range(0,5):
			if matrix[ctr][j][i] != '0':
				marked = 0
		if marked == 1:
			return 1

	
for line in sys.stdin:
	line = line.strip()
	if first == 0:
		nums = line.split(',')
		first = 1
	else:
		if line == '':
			none=0
			ctr +=1
		else:
			if none == 0:
				matrix.append([])	
				none = 1
			matrix[ctr].append(line.split())
		

draw = 0;
while draw < len(nums):
	for i in range(0,len(matrix)):
		for j in range(0,5):
			for k in range(0,5):
				if matrix[i][j][k] == nums[draw]:
					matrix[i][j][k] = '0'
	for k in range(0,len(matrix)):
		if hascomplete(k):
			score = calculatescore(k)
			print( score * int(nums[draw]))
			exit()
	draw += 1
		

