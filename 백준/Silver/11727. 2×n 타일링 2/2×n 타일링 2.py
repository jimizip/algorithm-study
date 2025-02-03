n = int(input())
if n == 0:
    print(0)
else:
    dp = [0] * (n+1)
    dp[1] = 1
    if n >= 2:  # n이 2 이상인 경우에만 dp[2] 초기화
        dp[2] = 3

    for i in range(3, n+1):
        dp[i] = (dp[i-2] * 2 + dp[i-1])

    print(dp[n] % 10007)