import math

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
cnt = 0

for i in range(N):
    cnt += 1

    tmp = A[i] - B

    # 올림 계산
    if tmp > 0:
        # cnt += (tmp + C - 1)
        cnt += math.ceil(tmp / C)

print(cnt)