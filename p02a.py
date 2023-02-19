# https://adventofcode.com/2021/day/2 part 1
# Created by: Menaka S. 2 Dec 2021

import sys 

currposh = 0
currposd = 0

for line in sys.stdin:
	line = line.strip()
	(inst,dist) = line.split(' ')
	if inst == 'forward':
		currposh += int(dist)
	if inst == 'down':
		currposd += int(dist)
	if inst == 'up':
		currposd -= int(dist)

#print(currposh , currposd)
print(currposh * currposd)
