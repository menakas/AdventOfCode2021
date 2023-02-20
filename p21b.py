# https://adventofcode.com/2021/day/21 part 2
# Created by: Menaka S. 21 Dec 2021

import sys
import copy
from collections import defaultdict

players = sys.stdin.read().splitlines()
rolls = 0
pos = []
score = [ 0, 0]

def increase_pos(val,incr):
	val += incr
	if val > 10:
		val = ((val - 1) %10) + 1
	return val

def roll_die():
	from itertools import product
	WIN = 21
	p1_wins = 0
	p2_wins = 0
	states = {(0,pos[0],0,pos[1]): 1}
	while len(states)>0:
		newstates = defaultdict(lambda: 0)
		for state,n in states.items():
			(score1,pos1,score2,pos2) = state
			for r1 in product([1,2,3],repeat=3):
				roll = sum(r1)
				p1_p_ = increase_pos(pos1,roll)
				p1_s_ = score1 + p1_p_
				if p1_s_ < WIN:
					for r2 in product([1,2,3],repeat=3):
						roll = sum(r2)
						p2_p_ = increase_pos(pos2,roll)
						p2_s_ = score2 + p2_p_
						if p2_s_ < WIN:
							newstates[(p1_s_,p1_p_,p2_s_,p2_p_)] += n
						else:
							p2_wins += n
				else:
					p1_wins += n
		states = newstates
		#print(states)
		#print("=================\n")
	return max(p1_wins,p2_wins)

turn = 0
universes = [dict(),dict()]
for i in range(2):
	pos.append(int(players[i].split(': ')[1]))
	universes[i][(pos[i],0)] = 1

print(roll_die()) 
