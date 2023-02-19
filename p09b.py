# https://adventofcode.com/2021/day/9 part 2
# Created by: Menaka S. 9 Dec 2021

import sys 

cols = 100
rows = 100
digits = []
lowpoints = []
basinsizes = []
basin = set()

def markbasin(posx,posy):
	global basin
	adj = []
	adj.append(getval(posx-1,posy))
	adj.append(getval(posx+1,posy))
	adj.append(getval(posx,posy+1))
	adj.append(getval(posx,posy-1))
	num = getval(posx,posy)
	if(adj[0] < 9 and (adj[0] > num)):
		markbasin(posx-1,posy)
		basin.add((posx-1,posy))
	if(adj[1] < 9 and (adj[1] > num)):
		markbasin(posx+1,posy)
		basin.add((posx+1,posy))
	if(adj[2] < 9 and (adj[2] > num)):
		markbasin(posx,posy+1)
		basin.add((posx,posy+1))
	if(adj[3] < 9 and (adj[3] > num)):
		markbasin(posx,posy-1)
		basin.add((posx,posy-1))

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


for i in range(rows):
	for j in range(cols):
		if islowpoint(i,j):
			lowpoints.append((i,j))
			markbasin(i,j)
			basin.add((i,j))
			basinsizes.append(len(basin))
			basin = set()

basinsizes.sort(reverse = True)
print(basinsizes[0] * basinsizes[1] * basinsizes[2])
