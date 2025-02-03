n = int(input())
dp = []
for _ in range(n):
    num = list(map(int, input().split()))
    dp.append(num)

for i in range(1, n):
    for j in range(i+1):
        if j == 0: # 맨 앞
            dp[i][j] += dp[i-1][j]
        elif j == i: # 맨 뒤
            dp[i][j] += dp[i-1][j-1]
        else:
            dp[i][j] += max(dp[i-1][j], dp[i-1][j-1])

print(max(dp[n-1]))