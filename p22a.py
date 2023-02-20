# https://adventofcode.com/2021/day/22 part 1
# Created by: Menaka S. 22 Dec 2021

import sys
import copy
from collections import defaultdict

lines = sys.stdin.read().splitlines()
cubes = defaultdict(lambda: 0)
totalct = 0
for line in lines:
	instr, dims = line.split(' ')
	dimx,dimy,dimz = dims.split(',')
	#print(dimx,dimy,dimz)
	x = dimx.split('=')[1].split('..')
	y = dimy.split('=')[1].split('..')
	z = dimz.split('=')[1].split('..')
	#print(x,y,z)
	if -50 <= int(x[0]) <= 50 and -50 <= int(x[1]) <= 50 and -50 <= int(y[0]) <= 50 and -50 <= int(y[1]) <= 50 and -50 <= int(z[0]) <= 50 and -50 <= int(z[1]) <= 50:
		for i in range(int(x[0]),int(x[1])+1):
			for j in range(int(y[0]),int(y[1])+1):
				for k in range(int(z[0]),int(z[1])+1):
					if instr == 'on':
						if cubes[(i,j,k)] == 0:
							cubes[(i,j,k)] = 1
							totalct += 1
							#print(i,j,k,totalct)
					else:
						if cubes[(i,j,k)] == 1:
							cubes[(i,j,k)] = 0
							totalct -= 1
							#print("Off",i,j,k,totalct)
							
					
print(totalct)
