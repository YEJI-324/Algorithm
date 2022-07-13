# 백준 4963 섬의 개수

# 1. 0 0 입력되기 전까지 지도 입력받기
# 2. w, h 입력 받고 > 지도 배열에 저장하기
# 3. 상하좌우, 대각선 체크하기


def dfs(x,y):
    if x <= -1 or x >= h or y <= -1 or y >= w:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        # 상하좌우
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        # 대각선
        dfs(x-1, y-1)
        dfs(x+1, y-1)
        dfs(x-1, y+1)
        dfs(x+1, y+1)
        return True
    return False

w,h = map(int, input().split())

while w != 0 and h != 0:
    graph = [[] for _ in range(h)]

    for i in range(h):
        graph[i] = list(map(int, input().split()))

    
    result = 0

    for i in range(h):
        for j in range(w):
            if dfs(i, j) == True:
                result += 1
    
    print(result)
    w,h = map(int, input().split())
