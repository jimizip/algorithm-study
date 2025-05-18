T = int(input())
for tc in range(1, T + 1):
    N, L = map(int, input().split())
    
    arr = [list(map(int, input().split())) for _ in range(N)]

    # DP[i]: i 칼로리 이하로 섭취했을 때 얻을 수 있는 최대 맛 점수
    dp = [0] * (L + 1)  # 인덱스 0부터 K까지 사용

    for i in arr:
        score, cal = i  # 현재 음식의 맛 점수와 칼로리
        
        # 역순으로 순회하여 중복 선택 방지 (0-1 배낭 문제 핵심)
        # 현재 음식의 칼로리(cal)부터 최대 허용 칼로리(K)까지 역순으로 확인
        for i in range(L, cal - 1, -1):
            # 기존 값(현재 음식 미선택) vs 현재 음식 선택 시 값 비교
            # DP[i - cal] + score: 현재 음식을 선택하면 (i-cal) 칼로리 상태에 현재 점수 추가
            dp[i] = max(dp[i], dp[i - cal] + score)

    print(f'#{tc} {dp[L]}')