# https://adventofcode.com/2021/day/7 part 2
# Created by: Menaka S. 7 Dec 2021

import sys 
import pprint 
from collections import defaultdict

mx = 2500

for line in sys.stdin:
	line = line.strip()
	crabs = list(map(int,line.split(',')))

ucrabs = set(crabs)
	
sums = defaultdict(lambda: 0)

for i in range(len(crabs)):
	for j in range(0,mx):
		n = abs(crabs[i] - j)
		sums[j] += int(n * (n+1) / 2)

print(min(sums.values()))
