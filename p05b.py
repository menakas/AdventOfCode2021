# https://adventofcode.com/2021/day/5 part 2
# Created by: Menaka S. 5 Dec 2021

import sys 

mx = 1000

matrix = [[0 for k in range(mx)] for j in range(mx)]

def count_safe():
	ct = 0
	for i in range(0,mx):
		for j in range(0,mx):
			if matrix[i][j] >=2:
				ct += 1
	return ct

def mark_matrix(line):
	(lhs,rhs) = line.split(' -> ')
	(x1,y1) = lhs.split(',')
	(x2,y2) = rhs.split(',')
	x1 = int(x1)
	x2 = int(x2)
	y1 = int(y1)
	y2 = int(y2)
	#print(x1,y1,"::",x2,y2)
	if abs(x1 - x2) == abs(y1 - y2):
		if x1 > x2:
			stepx = -1
			startx = x1
			endx = x2
			starty = y1
			if y1 > y2:
				endy = y2
				same = -1
			else:
				endy = y2
				same = 1
		else:
			stepx = 1
			startx = x1
			endx = x2
			starty = y1
			if y1 > y2:
				endy = y2
				same = -1
			else:
				endy = y2
				same = 1
		#print(startx,starty,endx,endy)
		for i in range(startx-startx,endx+stepx-startx,stepx):
			#print(startx+i,starty+(i*stepx*same))
			matrix[startx+i][starty+(i*stepx*same)] +=1
	if x1 == x2:
		if y2 > y1:
			for k in range(y1,y2+1):
				matrix[x1][k] += 1
		else:
			for k in range(y2,y1+1):
				matrix[x1][k] += 1
			
	if y1 == y2:
		if x2 > x1:
			for k in range(x1,x2+1):
				matrix[k][y1] += 1
		else:
			for k in range(x2,x1+1):
				matrix[k][y1] += 1
	#pprint.pprint(matrix)
			
for line in sys.stdin:
	line = line.strip()
	mark_matrix(line)
	
print(count_safe())
