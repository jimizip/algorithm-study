from collections import deque
MAX = 10 ** 5

N, M = map(int, input().split())
arr = [0] * ((MAX) + 1)

def bfs():
    Q = deque()
    Q.append(N)

    while Q:
        cn = Q.popleft()
        if cn == M:
            print(arr[cn]) # 시작점점
            break
        for i in (cn-1, cn+1, 2*cn):
            if 0 <= i <= MAX and not arr[i]:
                arr[i] = arr[cn] + 1
                Q.append(i)

bfs()