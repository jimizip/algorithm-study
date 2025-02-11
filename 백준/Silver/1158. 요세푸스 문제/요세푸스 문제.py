from collections import deque

N, K = map(int, input().split())

people = deque(range(1, N+1))

ans = []

while people:
    for _ in range(K-1):
        people.append(people.popleft())
    ans.append(people.popleft())

print(str(ans).replace('[', '<').replace(']' , '>'))