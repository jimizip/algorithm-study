import sys
input = sys.stdin.readline

# 입력
N = int(input())
D = [[0 for j in range(2)] for i in range(N+1)]

# 초기화
D[1][0] = 0
D[1][1] = 1

for i in range(2, N+1):
    D[i][0] = D[i-1][0] + D[i-1][1]
    D[i][1] = D[i-1][0]

# 출력
print(D[N][0] + D[N][1])