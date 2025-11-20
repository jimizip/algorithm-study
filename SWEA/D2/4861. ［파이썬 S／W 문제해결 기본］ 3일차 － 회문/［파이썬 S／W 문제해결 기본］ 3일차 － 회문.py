def is_palindrome(s):
    """문자열이 회문인지 확인"""
    n = len(s)
    for i in range(n // 2):  # 절반만 비교하면 됨
        if s[i] != s[n - 1 - i]:  # 대칭 위치 문자 비교
            return False
    return True


T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    board = [input().strip() for _ in range(n)]

    result = ""

    # 가로 방향 검사
    for i in range(n):
        for j in range(n - m + 1):
            substring = board[i][j:j + m]
            if is_palindrome(substring):
                result = substring
                break
        if result:
            break

    # 세로 방향 검사 (가로에서 못 찾았을 경우)
    if not result:
        for j in range(n): 
            for i in range(n - m + 1):
                substring = ''.join(board[i + k][j] for k in range(m))
                if is_palindrome(substring):
                    result = substring
                    break
            if result:
                break

    print(f"#{tc} {result}")
