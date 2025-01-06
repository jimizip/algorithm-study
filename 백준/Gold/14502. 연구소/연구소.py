import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
empty = []
virus = []

for i in range(N):
    row = list(map(int, input().split()))
    graph.append(row)
    for j in range(M):
        if row[j] == 0:
            empty.append((i, j))
        elif row[j] == 2:
            virus.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    que = deque(virus)
    visited = [[0] * M for _ in range(N)]
    count = len(empty) - 3

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = 1
                que.append((nx, ny))
                count -= 1

    return count

result = 0
for walls in combinations(empty, 3):
    for x, y in walls:
        graph[x][y] = 1
    
    result = max(result, bfs())
    
    for x, y in walls:
        graph[x][y] = 0

print(result)
