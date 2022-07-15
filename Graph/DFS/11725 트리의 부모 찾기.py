# 백준 11725 트리의 부모 찾기

import sys
sys.setrecursionlimit(10**6)

n = int(input())

graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for _ in range(n-1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(v, parent):

    if visited[v] == 0:
        visited[v] = parent
    
    for i in graph[v]:
        if visited[i] == 0:
            dfs(i, v)

dfs(1, 0)

for i in range(2, n+1):
    print(visited[i])