# https://adventofcode.com/2021/day/1
# Created by: Menaka S. 1 Dec 2021

import sys 

incA = 0
incB = 0
prev = -1
curr = -1
prevsum = -1
currsum = -1
nums = []

for line in sys.stdin:
	line = line.strip()
	nums.append(int(line))

for i in range(0,len(nums)-1):
	prev = nums[i] 
	curr = nums[i+1]
	if curr > prev:
		incA +=1

print(incA)

for i in range(0,len(nums)-3):
	prevsum = nums[i] + nums[i+1] + nums[i+2]
	currsum = nums[i+3] + nums[i+1] + nums[i+2]
	if currsum > prevsum:
		incB +=1

print(incB)
