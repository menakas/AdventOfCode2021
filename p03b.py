# https://adventofcode.com/2021/day/3 part 2
# Created by: Menaka S. 3 Dec 2021

import sys 

def binaryToDecimal(binary): 
    binary1 = binary 
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    return  decimal

ln = 0
oxynums = []
co2nums = []

for line in sys.stdin:
	line = line.strip()
	oxynums.append(line)
	co2nums.append(line)
	ln = len(line)

def calcpopular(curr):
	ones = 0
	for j in range(0,len(oxynums)):
		if oxynums[j][curr] == '1':
			ones += 1
	if ones >= len(oxynums)/2:
		return '1'
	else:
		return '0'

def calclpopular(curr):
	ones = 0
	for j in range(0,len(co2nums)):
		if co2nums[j][curr] == '1':
			ones += 1
	if ones >= len(co2nums)/2:
		return '0'
	else:
		return '1'

def retainpopular(curr,pop):
	rows = len(oxynums)
	rrows = []
	for j in range(0,rows):
		if oxynums[j][curr] != pop:
			rrows.append(j)
	for j in range(len(rrows)-1,-1,-1):
		oxynums.pop(rrows[j])

def retainlpopular(curr,pop):
	rows = len(co2nums)
	rrows = []
	for j in range(0,rows):
		if co2nums[j][curr] != pop:
			rrows.append(j)
	for j in range(len(rrows)-1,-1,-1):
		co2nums.pop(rrows[j])

for ind in range(0,ln):
	pop = calcpopular(ind)
	retainpopular(ind,pop)
	if len(oxynums) == 1:
		break


for ind in range(0,ln):
	pop = calclpopular(ind)
	retainlpopular(ind,pop)
	if len(co2nums) == 1:
		break

#print("====")
#print(oxynums)
#print(co2nums)
#print(binaryToDecimal(int(''.join(oxynums))))
#print(binaryToDecimal(int(''.join(co2nums))))
print(binaryToDecimal(int(''.join(oxynums))) * binaryToDecimal(int(''.join(co2nums))))
