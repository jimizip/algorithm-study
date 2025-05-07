import sys
sys.setrecursionlimit(10000)

N, M = map(int, input().split())
graph = [list(input()) for _ in range(M)]
w_cnt = 0
b_cnt = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(color, x, y):
    cnt = 1 # 현재 칸 포함
    graph[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] == color:
            cnt += dfs(color, nx, ny)
    return cnt

for i in range(M):
    for j in range(N):
        if graph[i][j] == 'W':
            w_cnt += dfs('W', i, j) ** 2
        elif graph[i][j] == 'B':
            b_cnt += dfs('B', i, j) ** 2

print(w_cnt, b_cnt)