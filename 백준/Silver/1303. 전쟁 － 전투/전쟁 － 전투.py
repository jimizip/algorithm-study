from collections import deque
N, M = map(int, input().split())
graph = [list(input()) for _ in range(M)]
w_cnt = 0
b_cnt = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(color, x, y):
    cnt = 0
    Q = deque()
    Q.append((x, y))
    graph[x][y] = 0

    while Q:
        x, y = Q.popleft()
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] == color:
                Q.append((nx, ny))
                graph[nx][ny] = 0
    
    return cnt

for i in range(M):
    for j in range(N):
        if graph[i][j] == 'W':
            w_cnt += bfs('W', i, j) ** 2
        elif graph[i][j] == 'B':
            b_cnt += bfs('B', i, j) ** 2

print(w_cnt, b_cnt)