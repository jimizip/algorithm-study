import sys
input = sys.stdin.readline

# 입력
N = int(input())

stairs = [0] * (N+1)

for i in range(1, N+1):
    stairs[i] = int(input())

# 초기화
dp = [0] * (N+1)
dp[1] = stairs[1]
if N >= 2:
    dp[2] = stairs[1] + stairs[2]
if N >= 3:
    dp[3] = max(stairs[1]+stairs[3], stairs[2]+stairs[3])

# 점화식
for i in range(4, N+1):
    dp[i] = max(dp[i-3] + stairs[i-1] + stairs[i], dp[i-2]+stairs[i])

# 출력
print(dp[N])