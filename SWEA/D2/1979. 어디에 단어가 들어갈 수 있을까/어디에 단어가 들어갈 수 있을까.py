T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    
    for i in range(N):
        tmp_row = 0
        for j in range(N):
            if board[i][j] == 1:
                tmp_row += 1
            if board[i][j] == 0 or j == N-1:
                if tmp_row == K:
                    cnt+=1
                tmp_row = 0

    for i in range(N):
        tmp_col = 0
        for j in range(N):
            if board[j][i] == 1:
                tmp_col += 1
            if board[j][i] == 0 or j == N-1:
                if tmp_col == K:
                    cnt +=1   
                tmp_col = 0     
    
    print(f'#{tc} {cnt}')