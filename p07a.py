# https://adventofcode.com/2021/day/7 part 1
# Created by: Menaka S. 7 Dec 2021

import sys 
import pprint 
from collections import defaultdict

mx = 2000

for line in sys.stdin:
	line = line.strip()
	crabs = list(map(int,line.split(',')))

ucrabs = set(crabs)
	
sums = defaultdict(lambda: 0)

for i in range(len(crabs)):
	for j in ucrabs:
		sums[j] += abs(crabs[i] - j)

print(min(sums.values()))
