# https://adventofcode.com/2021/day/2 part 2
# Created by: Menaka S. 2 Dec 2021

import sys 

currposh = 0
currposd = 0
curraim = 0

for line in sys.stdin:
	line = line.strip()
	(inst,dist) = line.split(' ')
	if inst == 'forward':
		currposh += int(dist)
		currposd += (int(dist) * curraim)
	if inst == 'down':
		curraim += int(dist)
	if inst == 'up':
		curraim -= int(dist)
	#print(line, "::", currposh , currposd, curraim)

#print(currposh , currposd)
print(currposh * currposd)
