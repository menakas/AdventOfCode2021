# https://adventofcode.com/2021/day/15 part 1
# Created by: Menaka S. 15 Dec 2021

import numpy as np
import sys 

lines = [list(map(int,list(line.strip()))) for line in sys.stdin]
mx = len(lines)
cost  =[[ 1000 for k in range(mx)] for j in range(mx)]

nlines = np.array(lines)

for i in range(1,5):
	addmat = [[ i for k in range(mx)] for j in range(mx)]
	naddmat = np.array(addmat)
	newlines = np.concatenate((nlines,(i+nlines-1)%9 + 1),axis=0)
	nlines = newlines
#print(nlines)
	

cost[0][0] = 0

def addnext(x,y):
	if x == 0 and y == 0:
		return
	if x == 0:
		cost[x][y] = cost[x][y-1] + lines[x][y]
	else:
		cost[x][y] = min(cost[x][y-1] + lines[x][y],cost[x-1][y] + lines[x][y])
	if y == 0:
		cost[x][y] = cost[x-1][y] + lines[x][y]
	else:
		cost[x][y] = min(cost[x-1][y] + lines[x][y],cost[x][y-1] + lines[x][y])

for i in range(len(lines)):
	for j in range(len(lines)):
		addnext(i,j)

print(cost[mx-1][mx-1])



