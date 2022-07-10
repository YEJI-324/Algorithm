# 백준 1012번 유기농 배추

# 1. TC 입력
# 2. 배추밭 크기 입력, 배추 수 입력
# 3. 배추 수 만큼 반복문 > 2차원 배열 채우기
# 4. 그래프 모양으로 모델링하기
# 5. result 출력하기
# 6. 2~6 TC 개수 만큼 반복

def dfs(x,y):
    if x <= -1 or x >= m or y <= -1 or y >= n:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

T = int(input())

for tc in range(T):
    m, n, k = map(int, input().split())

    graph = [[0] * n for i in range(m)]

    for i in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1
    
    result = 0

    for i in range(m):
        for j in range(n):
            if dfs(i, j) == True:
                result += 1
    
    print(result)