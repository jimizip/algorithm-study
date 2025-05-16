T = int(input())
for tc in range(1, T+1):
    board = [list(map(int, input().split())) for _ in range(9)]
    cnt = 0

    for i in range(9):
        # 행
        if sum(board[i]) != 45:
            cnt += 1
        # 열
        tmp = 0
        for j in range(9):
            tmp += board[j][i]
        if tmp != 45:
            cnt += 1

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            tmp = 0
            for row in range(3):
                for col in range(3):
                    tmp += board[row+i][col+j]
            if tmp != 45:
                cnt += 1
    
    if cnt > 0:
        print(f'#{tc} {0}')
    else:
        print(f'#{tc} {1}')