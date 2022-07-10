#백준 1260 DFS와 BFS

# 1. 노드 수 n
# 2. 엣지 수 m
# 3. 탐색 시작할 노드 번호 v
# 4. 간선 연결된 노드

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    if not visited[v]:
        print(v, end=' ')

    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

dfs(1)