import sys
input = sys.stdin.readline

# 입력
N = int(input())
D = [0] * (N+1)

# 초기화
D[1] = 0

for i in range(2, N+1):
    D[i] = D[i-1] + 1
    if i % 2 == 0:
        D[i] = min(D[i], D[i//2] + 1)
    if i % 3 == 0:
        D[i] = min(D[i], D[i//3] + 1)

# 출력
print(D[N])