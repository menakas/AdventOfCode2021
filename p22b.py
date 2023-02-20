# https://adventofcode.com/2021/day/22 part 2
# Created by: Menaka S. 22 Dec 2021

import sys
import copy
from collections import defaultdict,Counter

lines = sys.stdin.read().splitlines()
cubes = Counter()
totalct = 0
for line in lines:
	instr, dims = line.split(' ')
	dimx,dimy,dimz = dims.split(',')
	x = dimx.split('=')[1].split('..')
	y = dimy.split('=')[1].split('..')
	z = dimz.split('=')[1].split('..')
	for i in range(0,2):
		x[i] = int(x[i])
		y[i] = int(y[i])
		z[i] = int(z[i])
	on = 0
	if instr == 'on':
		on = 1
	else:
		on = -1
	newcubes = Counter()
	for cube,sign in cubes.items():
		(sx,ex,sy,ey,sz,ez) = cube
		#print(sx,ex,sy,ey,sz,ez)
	
		intx0 = max(sx,x[0])
		intx1 = min(ex,x[1])
		inty0 = max(sy,y[0])
		inty1 = min(ey,y[1])
		intz0 = max(sz,z[0])
		intz1 = min(ez,z[1])
		if intx0 <= intx1 and inty0 <= inty1 and intz0 <= intz1:
			newcubes[(intx0,intx1,inty0,inty1,intz0,intz1)] -= sign 
	if on > 0:
		newcubes[(x[0],x[1],y[0],y[1],z[0],z[1])] += on
			
	cubes.update(newcubes)
	#print(line,cubes)

totalct = 0
for coords,sign in cubes.items():
	sx,ex,sy,ey,sz,ez = coords
	totalct += ((ex-sx + 1) * (ey-sy+1) * (ez-sz+1) * sign)
print(totalct)
