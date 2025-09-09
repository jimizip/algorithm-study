from collections import deque

# 입력
N = int(input())
max_num = 0
g = []
result = []

for _ in range(N):
    low = list(map(int, input().split()))
    g.append(low)

    for i in low:
        if i > max_num:
            max_num = i

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(num, x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == 0 and g[nx][ny] > num:
                    visited[nx][ny] = 1
                    q.append((nx, ny))

for x in range(max_num):
    visited = [[0] * (N) for _ in range(N)]
    cnt = 0
    for j in range(N):
        for k in range(N):
            if g[j][k] > x and visited[j][k] == 0:
                bfs(x, j, k)
                cnt += 1

    result.append(cnt)

print(max(result))