N, K = map(int, input().split())

# dp[j] = 무게 한도가 j일 때의 최대 가치
dp = [0] * (K + 1)

for _ in range(N):
    w, v = map(int, input().split())
    
    for j in range(K, w - 1, -1):
        dp[j] = max(dp[j], v + dp[j - w])

print(dp[K])