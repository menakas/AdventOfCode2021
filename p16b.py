# https://adventofcode.com/2021/day/16 part 2
# Created by: Menaka S. 16 Dec 2021

import sys
import binascii
import math
from anytree import Node, RenderTree

line = sys.stdin.read()
line = line.strip()
ind = 0
stack = []


def hextobin(word):
	return ''.join([str(bin(int(c,16)))[2:].zfill(4) for c in word])


def binaryToDecimal(binary): 
    binary1 = binary
    decimal, ind, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, ind)  
        binary = binary//10
        ind += 1
    return  decimal

def decode(par):
	global ind

	if ind >= len(inp):
		return
	pversion = inp[ind:ind+3]
	ptypeid = inp[ind+3:ind+6]
	plengthtype = inp[ind+6]
	if ptypeid != '100': #operator
		oper = Node(ptypeid,parent=par)
		ind += 7
		#print("Operator")
		if plengthtype == '0':
			length = binaryToDecimal(int(inp[ind:ind+15]))
			#print("==Length of bits",inp[ind:ind+15],length)
			ind +=15
			length = ind+length
			while ind <length:
				decode(oper)
			ind = length
		else:
			num = binaryToDecimal(int(inp[ind:ind+11]))
			#print("==Num of subpackets",num)
			ind += 11
			for j in range(num):
				decode(oper)
	else: #literal
		ind += 6
		numstr = ''
		#print("Literal",inp[ind:])
		while inp[ind] == '1':
			numstr = numstr + inp[ind+1:ind+5]
			ind += 5
		numstr += inp[ind+1:ind+5]
		num = binaryToDecimal(int(numstr))
		operand = Node(num,parent=par)
		ind += 5
			
#print(line)
inp = hextobin(line)
while len(inp) %4:
	inp = '0' + inp
#print(inp,len(inp))	
root = Node("root")
decode(root)

#for pre, fill, node in RenderTree(root):
	#print("%s%s" % (pre, node.name))

def calc(par):
	if par.name == 'root':
		for child in par.children:
			return calc(child)
	if not par.children:
		return par.name
	if par.name == '000':
		return sum(calc(child) for child in par.children)
	if par.name == '001':
		return math.prod(calc(child) for child in par.children)
	if par.name == '010':
		return min(calc(child) for child in par.children)
	if par.name == '011':
		return max(calc(child) for child in par.children)
	childarr = [child for child in par.children]
	if par.name == '101':
		return int(calc(childarr[0]) > calc(childarr[1]))
	if par.name == '110':
		return int(calc(childarr[0]) < calc(childarr[1]))
	if par.name == '111':
		return int(calc(childarr[0]) == calc(childarr[1]))
		
print(calc(root))
