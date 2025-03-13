from collections import deque
				
N, M, V = map(int, input().split())
g = [[False] * (N+1) for _ in range(N+1)]

for i in range(M):
    x,y = map(int, input().split())
    g[x][y] = g[y][x] = 1

visitied1 = [False] * (N+1)
visitied2 = [False] * (N+1)

def dfs(V):
    visitied1[V] = True
    print(V, end=' ')
    for i in range(1, N+1):
        if not visitied1[i] and g[V][i]:
            dfs(i)

def bfs(V):
    q = deque([V])
    visitied2[V] = True
    while q:
        V = q.popleft()
        print(V, end=' ')
        for i in range(1, N+1):
            if not visitied2[i] and g[V][i]:
                q.append(i)
                visitied2[i] = True

dfs(V)
print()
bfs(V)