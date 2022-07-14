# 백준 2178 미로탐색

import sys
from collections import deque

n, m = map(int, input().split())

maze = [[] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

for i in range(n):
    maze[i] = list(map(int,sys.stdin.readline().rstrip()))

dxy = [ (0, -1), (0, +1), (-1, 0), (+1, 0) ]

q = deque([(0,0)])

while q:
    x, y = q.popleft()
    visited[x][y] = True

    for dx, dy in dxy:
        if x+dx < 0 or x+dx >= n or y+dy < 0 or y+dy >= m:
            continue
        if maze[x+dx][y+dy] == 1 and not visited[x+dx][y+dy]:
            q.append((x+dx, y+dy))
            visited[x+dx][y+dy] = True
            maze[x+dx][y+dy] = maze[x][y] +1

print(maze[n-1][m-1])