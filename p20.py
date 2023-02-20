# https://adventofcode.com/2021/day/20
# Created by: Menaka S. 20 Dec 2021

import sys
import copy

mx = 100
off = 100
step = 0
mxstep = 50
ctr = 0
matrix = [['.' for k in range(-off,mx+off)] for j in range(-off,mx+off)] 

def getneighbours(x,y):
	for i in range(x-1,x+2):
		for j in range(y-1,y+2):
			yield (i,j)

def getval(x,y):
	binstr = ''
	for (i,j) in getneighbours(x,y):
		if 0 <= i < len(matrix) and 0 <= j < len(matrix):
			binstr = binstr + str(int(matrix[i][j] == '#'))
	return int(binstr,2)
		
iea,_,*lines = sys.stdin.read().splitlines()

for line in lines:
	for i in range(len(line)):
		matrix[ctr+off][i+off] = line[i]
	ctr +=1

newmatrix = []
while step < mxstep:
	newmatrix = [[iea[getval(i,j)] for j in range(len(matrix[0]))] for i in range(len(matrix))]
	matrix = copy.deepcopy(newmatrix)
	ct = sum(int(matrix[i][j]=='#') for j in range(mxstep,len(matrix[0])-mxstep) for i in range(mxstep,len(matrix)-mxstep))
	step+=1
	if step in (2,50):
		print(ct)
