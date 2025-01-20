import sys
input = sys.stdin.readline

# 입력
T = int(input())
for _ in range(T):
    N = int(input())
    
    if N <= 3:
        if N == 1:
            print(1)
        elif N == 2:
            print(2)
        elif N == 3:
            print(4)
    else:
        dp = [0] * (N+1)
        dp[1], dp[2], dp[3] = 1, 2, 4

        for i in range(4, N+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

        print(dp[N])