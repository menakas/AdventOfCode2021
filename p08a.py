# https://adventofcode.com/2021/day/8 part 1
# Created by: Menaka S. 8 Dec 2021

import sys 
from collections import defaultdict

count = 0
digits = []
for line in sys.stdin:
	line = line.strip()
	(lhs,rhs) = line.split(' | ')
	digits = rhs.split()
	#print(list(filter(lambda digit: digit in [2,3,4,7], list(map(len,digits)))))
	count += len(list(filter(lambda digit: digit in [2,3,4,7], list(map(len,digits)))))

print(count)
	

