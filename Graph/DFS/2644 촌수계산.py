# 백준 2644번 촌수계산

# 1. n : 전체 사람 수
# 2. a, b : 계산 해야하는 두 사람
# 3. m : 관계 수
# 4. x, y : 부모 자식

# 1. 인접 리스트로 입력 받기(graph)
# 2. 3찾을 때 까지 탐색하기
# 3. 없으면 -1 출력

n = int(input())
a, b = map(int, input().split())
m = int(input())

visited = [False] * (n+1) 
graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

result = 0
flag = False

def dfs(v):
    global result, flag

    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            if i == b:
                flag = True
                result += 1
                return
            else:
                if not flag:
                    result += 1
                    dfs(i)
                    if not flag: result -= 1
                else: return

dfs(a)

print(result if flag else -1)