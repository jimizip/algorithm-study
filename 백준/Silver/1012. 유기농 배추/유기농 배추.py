import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, x, y):
    q = deque([(x, y)])  # 튜플로 좌표 추가
    graph[x][y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                q.append((nx, ny)) 
                graph[nx][ny] = 0

for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0]*M for _ in range(N)] 
    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1
    
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                bfs(graph, i, j)
                cnt += 1
    print(cnt)