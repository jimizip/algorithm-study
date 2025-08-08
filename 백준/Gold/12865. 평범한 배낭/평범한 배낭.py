N, K = map(int, input().split())
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

item = [[0,0]]
for _ in range(1, N+1):
    item.append(list(map(int, input().split())))

for i in range(1, N+1):
    for j in range(1, K+1):

        w = item[i][0]
        v = item[i][1]

        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], v + dp[i-1][j-w])

print(dp[N][K])