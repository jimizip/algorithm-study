import sys
input = sys.stdin.readline

def max_plums(T, W, plums):
    # T+1 x W+1 크기의 2차원 DP 테이블 생성
    dp = [[0] * (W + 1) for _ in range(T + 1)]
    
    for t in range(1, T + 1):
        # 1 또는 2
        plum = plums[t - 1]
        
        for w in range(W + 1):
            # 현재 위치 (w가 짝수면 1번 나무, 홀수면 2번 나무)
            current_tree = 1 if w % 2 == 0 else 2
            
            # 이동하지 않는 경우
            dp[t][w] = dp[t-1][w]
            
            # 이동하는 경우 (w > 0일 때만 가능)
            if w > 0:
                dp[t][w] = max(dp[t][w], dp[t-1][w - 1])
            
            # 현재 나무에서 자두를 받을 수 있는 경우
            if plum == current_tree:
                dp[t][w] += 1
    
    # 마지막 시간에서의 최대값 반환
    return max(dp[T])

# 입력
T, W = map(int, input().split())
# 각 시간마다 자두가 떨어지는 나무의 번호를 담고 있는 리스트
plums = [int(input()) for _ in range(T)]

# 출력
print(max_plums(T, W, plums))