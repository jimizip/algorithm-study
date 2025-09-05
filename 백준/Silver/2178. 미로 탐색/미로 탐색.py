from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

g = [list(map(int, input().strip())) for _ in range(N)]

def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque([(x, y, 1)])  # (x, y, distance)
    visited = [[False] * M for _ in range(N)]
    visited[x][y] = True

    while queue:
        x, y, dist = queue.popleft()
        if x == N-1 and y == M-1:  # 목표 지점에 도달하면 즉시 반환
            return dist
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and g[nx][ny] == 1 and not visited[nx][ny]:
                queue.append((nx, ny, dist + 1))
                visited[nx][ny] = True

    return -1 

print(bfs(0,0))