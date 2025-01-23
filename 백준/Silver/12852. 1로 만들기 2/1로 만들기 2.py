import sys
input = sys.stdin.readline

def min_dp(N):
    dp = [0] * (N+1)

    for i in range(2, N+1):
        dp[i] = dp[i-1] + 1
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3] + 1)
    
    return dp

def trace(N, dp):
    result = [N]
    while N > 1:
        if N % 3 == 0 and dp[N] == dp[N//3] + 1:
            N //= 3
        elif N % 2 == 0 and dp[N] == dp[N//2] + 1:
            N //= 2
        else:
            N-=1
        result.append(N)
    return result

# 입력
N = int(input())

dp = min_dp(N)

print(dp[N])
result = trace(N, dp)
print(*result)