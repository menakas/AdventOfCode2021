# https://adventofcode.com/2021/day/21 part 1
# Created by: Menaka S. 21 Dec 2021

import sys
import copy

players = sys.stdin.read().splitlines()
die = 0
rolls = 0
pos = []
score = [ 0, 0]
def increase_die():
	global die
	if die == 100:
		die = 1
	else:
		die += 1
	return die

def roll_die(player):
	global rolls
	for r in range(3):
		pos[player] += increase_die()
		if pos[player] >10:
			pos[player] = ((pos[player] -1) % 10) + 1
	rolls +=3
	score[player] += pos[player]
	if score[player] < 1000:
		return 1
	else:
		return 0

for i in range(2):
	pos.append(int(players[i].split(': ')[1]))

#print(pos)
#print(score)

turn = 0
while roll_die(turn): 
	if turn:
		turn = 0
	else:
		turn = 1
	#print(pos)
	#print(score)
if turn:
	print(rolls*score[0])
else:
	print(rolls*score[1])
