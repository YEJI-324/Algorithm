# 백준 11724 연결 요소의 개수

from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

result = 0

for i in range(1, n+1):
    if not visited[i]:
        result += 1
        queue = deque([i])
        while queue:
            v = queue.popleft()
            visited[v] = True

            for j in graph[v]:
                if not visited[j]:
                    queue.append(j)
                    visited[j] = True

print(result)