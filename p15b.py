# https://adventofcode.com/2021/day/15 part 2
# Created by: Menaka S. 15 Dec 2021

import os
import sys 
from collections import Counter, defaultdict
import heapq as heap

mx = 10
lines = []
risks = []
def split(word):
	return [int(char) for char in word]

for line in sys.stdin:
	line = line.strip()
	lines.append(line)


#print(lines)


k = [[*map(int, list(e))] for e in lines]
m = len(k)
n = len(k[0])

g = [[0] * 5 * n for _ in range(5 * m)]
for i in range(m):
    for j in range(n):
        g[i][j] = k[i][j]


for i in range(5 * m):
    for j in range(5 * n):
        source_row_idx = i
        source_col_idx = j

        if i >= m:
            source_row_idx = i - m
        
        if j >= n and i < m:
            source_col_idx = j - n

        val = g[source_row_idx][source_col_idx]
        
        if i >= m or j >= n:
            val += 1

        g[i][j] = val if val <= 9 else 1

m *= 5
n *= 5

dist = [[1000000] * n for _ in range(m)]
dist[0][0] = 0

visited = defaultdict(bool)
pq = []
heap.heappush(pq, (0, (0, 0)))

while pq:
    e = heap.heappop(pq)
    if e[1] == (m - 1, n - 1):
        print(dist[m - 1][n - 1])
        exit()
        
    visited[e[1]] = True

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    x,y = e[1]

    for k in range(4):
        xx = x + dx[k]
        yy = y + dy[k]

        if xx >= 0 and xx < m and yy >= 0 and yy < n and not visited[(xx,yy)]:
            if dist[xx][yy] > e[0] + g[xx][yy]:
                dist[xx][yy] = e[0] + g[xx][yy]
                heap.heappush(pq, (dist[xx][yy], (xx, yy)))
