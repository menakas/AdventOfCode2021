# https://adventofcode.com/2021/day/23
# Created by: Menaka S. 23 Dec 2021

import collections
import itertools
import math
import re

goal = {
	'A': 2,
	'B': 4,
	'C': 6,
	'D': 8,
}
goal_spaces = set(goal.values())
move_costs = {
	'A': 1,
	'B': 10,
	'C': 100,
	'D': 1000,
}


def can_reach(board, pos, dest):
	a = min(pos, dest)
	b = max(pos, dest)
	for i in range(a, b+1):
		if i == pos:
			continue
		if i in goal_spaces:
			continue
		if board[i] != '.':
			# print(' ', i, board[i][0], 'cannot reach')
			return False
	return True


def room_only_contains_goal(board, piece, dest):
	in_room = board[dest]
	return len(in_room) == in_room.count('.') + in_room.count(piece) 


def get_piece_from_room(room):
	for c in room:
		if c != '.':
			return c


def possible_moves(board, pos):
	piece = board[pos]
	# print(board, pos, piece)
	if pos not in goal_spaces:
		if can_reach(board, pos, goal[piece]) and room_only_contains_goal(board, piece, goal[piece]):
			return [goal[piece]]
		return []

	moving_letter = get_piece_from_room(piece)
	if pos == goal[moving_letter] and room_only_contains_goal(board, moving_letter, pos):
		return []

	possible = []
	for dest in range(len(board)):
		if dest == pos:
			continue
		if dest in goal_spaces and goal[moving_letter] != dest:
			continue
		if goal[moving_letter] == dest:
			if not room_only_contains_goal(board, moving_letter, dest):
				continue
		if can_reach(board, pos, dest):
			possible.append(dest)
	return possible


def add_to_room(letter, room):
	room = list(room)
	dist = room.count('.')
	assert dist != 0
	room[dist-1] = letter
	return ''.join(room), dist


def move(board, pos, dest):
	new_board = board[:]
	dist = 0
	moving_letter = get_piece_from_room(board[pos])
	if len(board[pos]) == 1:
		new_board[pos] = '.'
	else:
		new_room = ''
		found = False
		for c in board[pos]:
			if c == '.':
				dist += 1
				new_room += c
			elif not found:
				new_room += '.'
				dist += 1
				found = True
			else:
				new_room += c
		new_board[pos] = new_room
	
	dist += abs(pos - dest)

	if len(board[dest]) == 1:
		new_board[dest] = moving_letter
		return new_board, dist * move_costs[moving_letter]
	else:
		new_board[dest], addl_dist = add_to_room(moving_letter, board[dest])
		dist += addl_dist
		return new_board, dist * move_costs[moving_letter]


def solve(board):
	states = {tuple(board): 0}
	queue = [board]
	while queue:
		# print(len(queue))
		board = queue.pop()
		for pos, piece in enumerate(board):
			if get_piece_from_room(piece) is None:
				continue
			dests = possible_moves(board, pos)
			# print('{} ({}) can move to {}'.format(piece, pos, dests))
			for dest in dests:
				new_board, addl_cost = move(board, pos, dest)
				new_cost = states[tuple(board)] + addl_cost
				new_board_tuple = tuple(new_board)
				cost = states.get(new_board_tuple, 9999999)
				if new_cost < cost:
					# print(board, '->', new_board, ':', new_cost)
					states[new_board_tuple] = new_cost
					#print("_state",new_board,new_cost)
					queue.append(new_board)

	return states

board = ['.', '.', 'BC', '.', 'BC', '.', 'DA', '.', 'DA', '.', '.']
states = solve(board) 
print(states[('.', '.', 'AA', '.', 'BB', '.', 'CC', '.', 'DD', '.', '.')])

board = ['.', '.', 'BDDC', '.', 'BCBC', '.', 'DBAA', '.', 'DACA', '.', '.']
states = solve(board)
print(states[('.', '.', 'AAAA', '.', 'BBBB', '.', 'CCCC', '.', 'DDDD', '.', '.')])


