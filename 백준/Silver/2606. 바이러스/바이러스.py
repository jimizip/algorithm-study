from collections import deque

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    num1, num2 = map(int, input().split())
    graph[num1].append(num2)
    graph[num2].append(num1)

def bfs(x):
    visited[x] = 1
    Q = deque([x])

    while Q:
        c = Q.popleft()
        for n in graph[c]:
            if visited[n] == 0:
                Q.append(n)
                visited[n] = 1
    
    return sum(visited)-1

print(bfs(1))