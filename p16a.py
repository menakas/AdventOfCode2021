# https://adventofcode.com/2021/day/16 part 1
# Created by: Menaka S. 16 Dec 2021

import sys
import binascii

line = sys.stdin.read()
line = line.strip()
ind = 0
vtotal = 0

def hextobin(word):
	scale = 16 ## equals to hexadecimal
	num_of_bits = 16
	return bin(int(word, scale))[2:].zfill(num_of_bits)


def binaryToDecimal(binary): 
    binary1 = binary
    decimal, ind, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, ind)  
        binary = binary//10
        ind += 1
    return  decimal

def decode():
	global vtotal
	global ind

	if ind >= len(inp):
		return
	pversion = inp[ind:ind+3]
	vtotal += binaryToDecimal(int(pversion))
	ptypeid = inp[ind+3:ind+6]
	plengthtype = inp[ind+6]
	#print("\n....Decoding",ind,pversion,ptypeid,plengthtype,vtotal)
	if ptypeid != '100': #operator
		ind += 7
		#print("Operator")
		if plengthtype == '0':
			length = binaryToDecimal(int(inp[ind:ind+15]))
			#print("==Length of bits",inp[ind:ind+15],length)
			ind +=15
			length = ind+length
			while ind <length:
				decode()
			ind = length
		else:
			num = binaryToDecimal(int(inp[ind:ind+11]))
			#print("==Num of subpackets",num)
			ind += 11
			for j in range(num):
				decode()
	else: #literal
		ind += 6
		numstr = ''
		#print("Literal",inp[ind:])
		while inp[ind] == '1':
			numstr = numstr + inp[ind+1:ind+5]
			ind += 5
		numstr += inp[ind+1:ind+5]
		num = binaryToDecimal(int(numstr))
		#print(numstr,num)
		ind += 5
			
#print(line)
inp = hextobin(line)
while len(inp) %4:
	inp = '0' + inp
#print(inp)	
decode()
print(vtotal)

	

