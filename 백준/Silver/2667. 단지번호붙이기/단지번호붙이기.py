from collections import deque

N = int(input())
graph = []
result = []

for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(graph, a, b):
    Q = deque()
    Q.append([a, b])
    graph[a][b] = 0
    count = 1

    while Q:
        x, y = Q.popleft()
        graph[x][y] = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if nx < 0 or nx >= len(graph) or ny < 0 or ny >= len(graph):
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                Q.append([nx, ny])
                count += 1
    
    return count

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            count = bfs(graph, i, j)
            result.append(count)

result.sort()

print(len(result))
for r in result:
    print(r)