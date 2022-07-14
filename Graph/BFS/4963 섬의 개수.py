# 백준 4963 섬의 개수

# 1. 0 0 입력되기 전까지 지도 입력받기
# 2. w, h 입력 받고 > 지도 배열에 저장하기
# 3. 상하좌우, 대각선 체크하기

from collections import deque

def dfs(x,y):
    if x <= -1 or x >= h or y <= -1 or y >= w:
        return False
    if m[x][y] == 1:
        m[x][y] = 0
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

def bfs():
    
    dxy = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    bfs_result = 0

    for i in range(h):
        for j in range(w):
            if m[i][j] == 1 and not visited[i][j]:
                queue = deque([(i, j)])
                bfs_result += 1
                print(queue, bfs_result)

                while queue:
                    x, y = queue.popleft()
                    visited[x][y] = True

                    for dx, dy in dxy:
                        if x+dx < 0 or x+dx >= h or y+dy < 0 or y+dy >= w:
                            continue
                        if m[x+dx][y+dy] == 1 and not visited[x+dx][y+dy]:
                            queue.append((x+dx, y+dy))
                            visited[x+dx][y+dy] = True
            
    print(bfs_result)

w,h = map(int, input().split())

while w != 0 and h != 0:
    m = [[] for _ in range(h)]

    for i in range(h):
        m[i] = list(map(int, input().split()))

    visited = [[False for _ in range(w)] for _ in range(h)]
    bfs()

    dfs_result = 0

    for i in range(h):
        for j in range(w):
            if dfs(i, j) == True:
                dfs_result += 1
    

    print(dfs_result)
    w,h = map(int, input().split())
