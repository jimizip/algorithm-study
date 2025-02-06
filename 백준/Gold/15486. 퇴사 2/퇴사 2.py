import sys
input = sys.stdin.readline

N = int(input())
slist = [tuple(map(int, input().split())) for _ in range(N)]
dp = [0 for _ in range(N+1)]

for i in range(N-1, -1, -1):
    t, p = slist[i]
    if i + t > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], p + dp[i+t])

print(dp[0])