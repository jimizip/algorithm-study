def backtrack(row, total, used, arr, n, min_sum):

    # 가지치기: 현재 합이 이미 최솟값보다 크면 종료
    if total >= min_sum[0]:
        return

    # 기저 조건: 모든 행을 선택했으면
    if row == n:
        min_sum[0] = min(min_sum[0], total)
        return

    # 현재 행에서 각 열을 시도
    for col in range(n):
        if not used[col]:  # 아직 사용하지 않은 열이면
            used[col] = True  # 열 선택
            backtrack(row + 1, total + arr[row][col], used, arr, n, min_sum)
            used[col] = False  # 백트래킹: 선택 취소


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    used = [False] * n  # 각 열의 사용 여부
    min_sum = [float('inf')]  # 최솟값 (리스트로 참조 전달) or global

    backtrack(0, 0, used, arr, n, min_sum)

    print(f"#{tc} {min_sum[0]}")
