import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [[False] * m for _ in range(n)]
year = 0

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    melt_num[x][y] += 1
                
                if not visited[nx][ny] and graph[nx][ny] != 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = True


while True:
    melt_num = [[0] * m for _ in range(n)]             
    cnt = 0  
    visited = [[False] * m for _ in range(n)]

    for i in range(n): # 한 덩이가 나눠졌는지 cnt로 기록
        for j in range(m):
            if graph[i][j] != 0 and not visited[i][j]:
                bfs(i, j)
                cnt += 1

    for i in range(n): # 1 년 후에 빙하가 녹은 높이 반영
        for j in range(m):
            if melt_num[i][j]:
                graph[i][j] -= melt_num[i][j]
                if graph[i][j] < 0:
                    graph[i][j] = 0
    year += 1

    if cnt == 0: # 나눠지지 않고 한 덩이가 바로 다 녹았다면 0 출력 후 종료
        print(0)
        break

    if cnt >= 2: # 두 덩이 이상으로 나눠졌다면 걸린 년수 출력 후 종료
        print(year - 1)
        break