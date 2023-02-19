# https://adventofcode.com/2021/day/12 part 1
# Created by: Menaka S. 12 Dec 2021

import sys 

lines = []
graph = set()
bigcaves = []

def isbigcave(word):
	ucase = 1
	for i in range(len(word)):
		if word[i].upper() != word[i]:
			ucase = 0
	return ucase

def addnext(given,path):
	for (st,ed) in graph:
		if st == given:
			if ed not in bigcaves and path.find(',' + ed) > 0:
				continue
			if ed == 'end':
				paths.add(path + ',' + ed)
			else:
				addnext(ed,path + ',' + ed)
			

for line in sys.stdin:
	line = line.strip()
	(lhs,rhs) = line.split('-')
	if rhs == 'start':
		lhs, rhs = rhs, lhs
	graph.add((lhs,rhs))
	if lhs != 'start' and rhs != 'end':
		graph.add((rhs,lhs))
	if isbigcave(lhs):
		bigcaves.append(lhs)
	if isbigcave(rhs):
		bigcaves.append(rhs)
	

#print(graph)
#print(bigcaves)

paths = set()

given = 'start'
addnext(given,'start')


print(len(paths))


