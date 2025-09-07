from collections import deque

N = int(input())
a, b = map(int, input().split())
M = int(input())
g = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    x, y = map(int, input().split())
    g[x].append(y)
    g[y].append(x)

def bfs(a, b):
    q = deque()
    q.append(a)
    visited[a] = 1

    while q:
        cn = q.popleft()

        if cn == b:
            return visited[b] - 1

        for i in range(1, N+1):
            if not visited[i]:
                if i in g[cn]:
                    visited[i] = visited[cn] + 1
                    q.append(i)

    return -1

print(bfs(a, b))