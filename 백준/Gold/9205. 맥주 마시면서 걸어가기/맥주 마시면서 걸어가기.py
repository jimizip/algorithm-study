from collections import deque

T = int(input())
for _ in range(T):

    def bfs():
        q = deque()
        q.append((home_x, home_y))
        while q:
            x, y = q.popleft()
            if (abs(x - end_x) + abs(y - end_y)) <= 1000:
                return "happy"
            for i in range(N):
                if visited[i] == 0:
                    new_x, new_y = store[i]
                    if (abs(x-new_x) + abs(y-new_y)) <= 1000:
                        visited[i] = 1
                        q.append((new_x, new_y))
        return "sad"


    N = int(input())
    home_x, home_y = map(int, input().split())
    store = []
    for _ in range(N):
        a, b = map(int, input().split())
        store.append((a, b))
    end_x, end_y = map(int, input().split())
    visited = [0] * (N+1)
    print(bfs())