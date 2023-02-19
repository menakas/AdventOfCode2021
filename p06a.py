# https://adventofcode.com/2021/day/6 part 1
# Created by: Menaka S. 6 Dec 2021

import sys 

mx = 80

def change_state():
	more = []
	for i in range(0,len(lfish)):
		lfish[i] -= 1
		if lfish[i] == -1:
			lfish[i] = 6
			more.append(8)
	if len(more) > 0:
		for x in more:
			lfish.append(x)
			
for line in sys.stdin:
	line = line.strip()
	lfish = list(map(int,line.split(',')))
	
day = 0

while day < mx:
	change_state()
	day += 1

print(len(lfish))



