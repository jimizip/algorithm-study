from collections import deque

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    score = deque(list(map(int, input().split())))
    inx = deque(range(N))
    cnt = 0

    while score:
        if score[0] < max(score):
            score.append(score.popleft())
            inx.append(inx.popleft())
        elif score[0] == max(score):
            score.popleft()
            cnt += 1
            if inx.popleft() == M:
                print(cnt)
                break