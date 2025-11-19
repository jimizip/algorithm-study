T = int(input())
for tc in range(1, T+1):
    n, l = map(int, input().split()) 
    
    dp = [0] * (l + 1)
    
    for _ in range(n):
        t, k = map(int, input().split()) 
        
        for w in range(l, k-1, -1): 
            # max(현재 값, 이 재료를 추가한 경우)
            dp[w] = max(dp[w], dp[w-k] + t)
    
    print(f"#{tc} {dp[l]}")
