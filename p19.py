# https://adventofcode.com/2021/day/19
# Created by: Menaka S. 19 Dec 2021

import sys
import copy
from itertools import combinations
import re
import math
import numpy as np

scanners = []
def rotations():
	vectors = [ (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1), ]
	vectors = list(map(np.array, vectors))
	for vi in vectors:
		for vj in vectors:
			if vi.dot(vj) == 0:
				vk = np.cross(vi, vj)
				yield lambda x: np.matmul(x, np.array([vi, vj, vk]))


def fit(scanners, hashes, i, j, v):
	s1, s2 = scanners[i], scanners[j]
	for rot in rotations():
		s2t = rot(s2)
		p = hashes[i][v][0]
		for q in hashes[j][v]:
			diff = s1[p, :] - s2t[q, :]
			if len((b := set(map(tuple, s2t + diff))) & set(map(tuple, s1))) >= 12:
				return diff, b, rot


def map_hash(coords):
	s = {
		tuple(sorted(map(abs, coords[i, :] - coords[j, :]))): (i, j)
		for i, j in combinations(range(len(coords)), 2)
	}
	return s

def match(scanners, hashes):
	for i, j in combinations(range(len(hashes)), 2):
		if len(m := set(hashes[i]) & set(hashes[j])) >= math.comb(12, 2):
			yield i, j, next(iter(m))


def solve(scanners):
	scanners = copy.deepcopy(scanners)
	positions = {0: (0, 0, 0)}
	hashes = list(map(map_hash, scanners))
	beacons = set(map(tuple, scanners[0]))
	while len(positions) < len(scanners):
		for i, j, v in match(scanners, hashes):
			if not (i in positions) ^ (j in positions):
				continue
			elif j in positions:
				i, j = j, i
			positions[j], new_beacons, rot = fit(scanners, hashes, i, j, v)
			scanners[j] = rot(scanners[j]) + positions[j]
			beacons |= new_beacons
	return [positions[i] for i in range(len(scanners))], beacons


for line in sys.stdin:
	line = line.strip()
	if line == "":
		continue
	scanner = re.match(r".*scanner (\d+).*",line)
	if scanner:
		scannerid = scanner[1]
		scanners.append([])
		continue
	else:
		x,y,z = line.split(',')
		scanners[-1].append((int(x),int(y),int(z))) #2d array of tuples #first d is each scanner #2nd d is list of beacons

scanners = [np.array(x) for x in scanners]
#print(scanners)
positions, beacons = solve(scanners)
print(len(beacons))
print(max(np.abs(x - y).sum() for x, y in combinations(positions, 2)))
