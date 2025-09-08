from collections import deque

N = int(input())
max_num = 0
graph = []

for _ in range(N):
    low = list(map(int, input().split()))
    graph.append(low)

    for i in low:
        if i > max_num:
            max_num = i

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y, num):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] > num and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))

result = []

for i in range(max_num):
    cnt = 0
    visited = [[0] * N for _ in range(N)]
    for j in range(N):
        for k in range(N):
            if graph[j][k] > i and visited[j][k] == 0:
                bfs(j, k, i)
                cnt += 1
    result.append(cnt)

print(max(result))