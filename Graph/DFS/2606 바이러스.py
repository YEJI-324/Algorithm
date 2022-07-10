#백준 2606번 바이러스

# 1. 컴퓨터 수
# 2. 연결되어 있는 컴퓨터 쌍 수
# 3. 컴퓨터 번호 쌍
# 1번 컴퓨터가 웜 바이러스에 걸렸을 때, 바이러스에 걸리게 되는 컴퓨터 수

num_computer = int(input())
num_pair = int(input())

virus = [False] * (num_computer + 1)
graph = [[]*num_computer for _ in range(num_computer + 1)]

for _ in range(num_pair):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = 0
def dfs(v):
    global result
    
    virus[v] = True
    for i in graph[v]:
        if not virus[i]:
            dfs(i)
            result += 1


dfs(1)

print(result)