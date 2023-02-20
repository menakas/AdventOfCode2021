# https://adventofcode.com/2021/day/17 part 2
# Created by: Menaka S. 17 Dec 2021

#Slow code; Need to work on performance

import sys

line = sys.stdin.read().strip()
parts = line.split('=')
parts[1] = parts[1].split(', ')[0]
tx =parts[1].split('..')
ty =parts[2].split('..')
tstartx = int(tx[0])
tendx = int(tx[1])
tstarty = int(ty[0])
tendy = int(ty[1])
if tstartx > tendx:
	tstartx, tendx = tendx, tstartx
if tstarty > tendx:
	tstarty, tendy = tendy, tstarty

maxsteps = 500
ivs = set()

def calctrajectory(x,y,i,j,step):
	while step <= maxsteps:
		x += i
		y += j
		if i > 0:
			i -= 1
		elif i < 0:
			i += 1 
		j -= 1
		step += 1
		if tstartx <= x <= tendx and tstarty <= y <= tendy:
			return 1
	
mx = 300
for i in range(-mx,mx):
	for j in range(-mx,mx):
		if calctrajectory(0,0,i,j,0):
			ivs.add((i,j))

print(len(ivs))


