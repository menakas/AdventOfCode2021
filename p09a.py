# https://adventofcode.com/2021/day/9 part 1
# Created by: Menaka S. 9 Dec 2021

import sys 

cols = 100
rows = 100
digits = []

def split(word):
    return [int(char) for char in word]

def getval(posx,posy):
	if posx >=0 and posy >= 0 and posx < rows and posy < cols:
		return digits[posx][posy]
	else:
		return 10
		
def islowpoint(posx,posy):
	adj = []
	adj.append(getval(posx-1,posy))
	adj.append(getval(posx+1,posy))
	adj.append(getval(posx,posy+1))
	adj.append(getval(posx,posy-1))
	num = getval(posx,posy)
	for k in range(0,4):
		if adj[k] <= num:
			return 0
	return 1

for line in sys.stdin:
	digits.append(split(line.strip()))

risklevel = 0

for i in range(rows):
	for j in range(cols):
		if islowpoint(i,j):
			risklevel += getval(i,j) + 1

print(risklevel)
	
	

