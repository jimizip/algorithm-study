N = int(input())

dp = [[0] * 10 for _ in range(N+1)]

for i in range(1, 10):
    dp[1][i] = 1

# 길이가 i 이고 마지막 숫자가 j인 계단 수의 개수
for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            dp[i][0] = dp[i-1][1]
        elif j == 9:
            dp[i][9] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
    
result = sum(dp[N]) % 1000000000
print(result)