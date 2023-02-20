# https://adventofcode.com/2021/day/18 part 2
# Created by: Menaka S. 18 Dec 2021

import sys
from ast import literal_eval
import copy
import math
import re

mylist = []
mystr = ''
first = 1

def is_other_char(char):
	if char in ('[',']',','):
		return 1
	return 0

def parseinp(text):
	if text and is_other_char(text[0]):
		mylist.append(text[0])
		parseinp(text[1:])
	else:
		mtext = re.match(r"^(\d+)",text)
		if mtext:
			mylist.append(int(mtext[0]))
			parseinp(text[len(mtext[0]):])

def mysplit():
	global mylist
	newlist = []
	alreadysplit = 0
	for i in range(len(mylist)):
		if is_other_char(mylist[i]):
			newlist.append(mylist[i])
		elif mylist[i] < 10:
			newlist.append(mylist[i])
		else:
			if not alreadysplit:
				#print(mylist[i],"splitting")
				newlist.extend(['[',math.floor(mylist[i]/2),',',math.ceil(mylist[i]/2),']'])
				alreadysplit = 1
			else:
				newlist.append(mylist[i])
	mylist = copy.deepcopy(newlist)
	#print(''.join(str(e) for e in mylist))

def myreduce(level,ind):
	global mylist
	while( ind < len(mylist)):
		if mylist[ind] == '[':
			level += 1
		if mylist[ind] == ']':
			level -= 1
		if level >= 5:
			needsplit = 0
			lhs = mylist[ind+1]
			rhs = mylist[ind+3]
			j = ind
			#print(lhs,rhs)
			while j >=0:
				if isinstance(mylist[j],int):
					#print(lhs,"lll")
					mylist[j] += lhs
					break
				j -=1
			j = ind+4
			while j < len(mylist):
				if isinstance(mylist[j],int):
					#print(rhs,"rrrr")
					mylist[j] += rhs
					break
				j +=1
			mylist = mylist[:ind] +[0] + mylist[ind+5:]
			#print(''.join(str(e) for e in mylist))
			level -=1
		ind +=1


def getmagnitude(lst):
	#print(lst)
	if isinstance(lst[0],int) and isinstance(lst[1],int):
		return (3 * lst[0]) + (2 * lst[1])
	elif isinstance(lst[0],list) and isinstance(lst[1],int):
		return (3 * getmagnitude(lst[0])) + (2 * lst[1])
	elif isinstance(lst[0],int) and isinstance(lst[1],list):
		return (3 * lst[0]) + (2 * getmagnitude(lst[1]))
	else:
		return (3 * getmagnitude(lst[0])) + (2 * getmagnitude(lst[1]))


nums =[] 	

for line in sys.stdin:
	line = line.strip()
	mylist = []
	parseinp(line)
	nums.append(copy.deepcopy(mylist))

maxmag = 0
for i in range(len(nums)):
	for j in range(len(nums)):
		#print(i,j)
		if i != j:
			mylist = []
			mylist.append('[')
			mylist.extend(nums[i])
			mylist.append(',')
			mylist.extend(nums[j])
			mylist.append(']')
			#print("==>",''.join(str(e) for e in mylist))
			while True:
				oldlist = copy.deepcopy(mylist)
				myreduce(0,0)
				mysplit()
				if mylist == oldlist:
					break
			#print(''.join(str(e) for e in mylist))
			mlist = literal_eval(''.join(str(e) for e in mylist))
			#print(mlist)
			mag = getmagnitude(mlist)
			#print("Mgni",i,j,mag)
			if mag > maxmag:
				maxmag = mag
print(maxmag)
	
