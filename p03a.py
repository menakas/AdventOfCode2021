# https://adventofcode.com/2021/day/3 part 1
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
gamma = []
epsilon = []
nums = []

for line in sys.stdin:
	line = line.strip()
	nums.append(line)
	ln = len(line)

rows = len(nums)

for i in range(0,ln):
	gamma.append(0)
	epsilon.append(0)
	for j in range(0,len(nums)):
		if nums[j][i:i+1] == '1':
			gamma[i] += 1

	

#print(gamma)	
for i in range(0,ln):
	if (gamma[i] > rows/2):
		gamma[i] = '1'
		epsilon[i] = '0'
	else:
		gamma[i] = '0'
		epsilon[i] = '1'
#print(gamma)	
#print(epsilon)	

gammab = int(''.join(gamma))
epsilonb = int(''.join(epsilon))
#print(gammab)	
#print(epsilonb)	
	
#print(binaryToDecimal(gammab))
#print(binaryToDecimal(epsilonb))
print(binaryToDecimal(gammab)*binaryToDecimal(epsilonb))

