from collections import deque

N, M = map(int, input().split())
arr = []
for i in range(1, N+1):
    arr.append(i)
Q = deque(arr)

position = list(map(int, input().split()))

cnt = 0
while len(position) != 0:
    if position[0] == Q[0]:
        position.remove(position[0])
        Q.popleft()
        continue
    elif Q.index(position[0]) > len(Q) // 2:
        Q.appendleft(Q.pop())
        cnt += 1
    else:
        Q.append(Q.popleft())
        cnt += 1
    

print(cnt)