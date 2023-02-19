# https://adventofcode.com/2021/day/6 part 2
# Created by: Menaka S. 6 Dec 2021

from collections import Counter
from sys import stdin

fish = Counter([int(n) for n in stdin.readline().split(',')])

for i in range(256):
	next_fish = Counter()
	for k, v in fish.items():
		if k == 0:
		    next_fish[6] += v
		    next_fish[8] += v
		else:
		    next_fish[k - 1] += v
	fish = next_fish

print(sum(fish.values()))
