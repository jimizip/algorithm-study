from collections import deque

N = int(input())
arr = []

for i in range(1, N+1):
    arr.append(i)

Q = deque(arr)
while len(Q) != 1:
    Q.popleft()
    Q.append(Q.popleft())

print(Q[0])