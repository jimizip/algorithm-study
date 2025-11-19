T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [[0]*10 for _ in range(10)]
    for _ in range(N):
        ls, le, rs, re, color = map(int, input().split())
        if color == 1:
            for i in range(ls, rs+1):
                for j in range(le, re+1):
                    board[i][j] += 1
        else:
            for i in range(ls, rs+1):
                for j in range(le, re+1):
                    board[i][j] += 2

    result = 0
    for i in range(10):
        for j in range(10):
            if board[i][j] == 3:
                result += 1

    print(f'#{tc} {result}')