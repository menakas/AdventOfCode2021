# https://adventofcode.com/2021/day/13
# Created by: Menaka S. 13 Dec 2021

import sys 

folds = []
fold = 0
points = set()

for line in sys.stdin:
	line = line.strip()
	if line == '':
		fold = 1
		continue
	if fold:
		(lhs,rhs) = line.split('=')
		rhs = int(rhs)
		lhs = lhs[-1:]
		folds.append((lhs,rhs))
	else:
		(x,y) = line.split(',')
		points.add((int(x),int(y)))


first = 1
for fold in folds:
	(l,r) = fold
	if l == 'x':
		fold = set((x,y) for (x,y) in points if x > int(r))
		points = points - fold
		points = points.union(set(((2 * int(r)) - x,y) for (x,y) in fold))
	if l == 'y':
		fold = set((x,y) for (x,y) in points if y > int(r))
		points = points - fold
		points = points.union(set((x, (2 * int(r)) - y) for (x,y) in fold))
	if first:
		print(len(points))
		first = 0

max_y  = max(map(lambda x: x[1], points))
max_x  = max(map(lambda x: x[0], points))
#print(max_x,max_y)

for i in range(max_y+1):
	line = ''
	for j in range(max_x+1):
		if (j,i) in points:
			line = line + '#'
		else:
			line = line + '.'
	print(line)


