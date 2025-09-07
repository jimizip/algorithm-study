from collections import deque

F, S, G, U, D = map(int, input().split())
g = [0] * (F+U+1)

def bfs():
    q = deque()
    q.append(S)
    g[S] = 1

    while q:
        cn = q.popleft()

        if cn == G:
            return g[cn] - 1

        for i in ((cn + U), (cn - D)):
            if g[i] == 0 and 0 < i <= F:
                g[i] = g[cn] + 1
                q.append(i)

    return "use the stairs"

print(bfs())