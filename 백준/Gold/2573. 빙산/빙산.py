from collections import deque

# 입력
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
year = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(a, b):
    q = deque()
    q.append((a, b))
    visited[a][b] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    melt[x][y] += 1
                else:
                    visited[nx][ny] = 1
                    q.append((nx, ny))


while True:
    visited = [[0] * M for _ in range(N)]
    melt = [[0] * M for _ in range(N)]
    count = 0

    for i in range(1, N-1):
        for j in range(1, M-1):
            if graph[i][j] > 0 and visited[i][j] == 0:
                bfs(i, j)
                count += 1

    for i in range(1, N-1):
        for j in range(1, M-1):
            graph[i][j] -= melt[i][j]
            if graph[i][j] < 0:
                graph[i][j] = 0

    if count >= 2:
        print(year)
        break
    elif count == 0:
        print(0)
        break

    year += 1
