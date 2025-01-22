# 입력
N = int(input())

if N == 1:
    print(1)
else:
    dp = [0] * (N+1)

    # 초기화
    dp[1] = 1
    dp[2] = 2

    # 점화식
    for i in range(3, N+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 10007

    # 출력
    print(dp[N])