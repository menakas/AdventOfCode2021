# https://adventofcode.com/2021/day/17 part 1
# Created by: Menaka S. 17 Dec 2021

import sys
import binascii

line = sys.stdin.read()
line = line.strip()
parts = line.split('=')
parts[1] = parts[1].split(', ')[0]
tx =parts[1].split('..')
ty =parts[2].split('..')
tstartx = int(tx[0])
tendx = int(tx[1])
tstarty = int(ty[0])
tendy = int(ty[1])
if tstartx > tendx:
	temp = tstartx
	tstartx = tendx
	tendx = temp
if tstarty > tendx:
	temp = tstarty
	tstarty = tendx
	tendy = temp
#print(tstartx,tendx,tstarty,tendy)


maxy = -1000
maxsteps = 800

def is_in_target(x,y):
	global tstartx, tstarty, tendx, tendy
	if tstartx <= x <= tendx and tstarty <= y <= tendy:
		return 1
	return 0


def calctrajectory(x,y,i,j,step):
	global currentmax, intarget
	if step >= maxsteps:
		return
	x += i
	y += j
	if i > 0:
		i -= 1
	elif i < 0:
		i += 1 
	j -= 1
	if y > currentmax:
		currentmax = y
	step += 1
	if is_in_target(x,y):
		intarget = 1
		#print(x,y,i,j,step)
		#print("....In target")
	calctrajectory(x,y,i,j,step)
	
mx = 100
for i in range(-mx,mx):
	for j in range(-mx,mx):
		currentmax = -1000
		intarget = 0
		calctrajectory(0,0,i,j,0)
		if currentmax > maxy and intarget:
			maxy = currentmax
			ivx = i
			ivy = j

print(maxy) #,ivx,ivy)


