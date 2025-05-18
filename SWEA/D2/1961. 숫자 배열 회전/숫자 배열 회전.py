T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    new = [[0]*N for _ in range(N)]
    result_90 = []
    result_180 = []
    result_270 = []

    # 90
    for i in range(N):
        tmp = ''
        for j in range(N-1, -1, -1):
            new[i][j] = board[j][i]
            tmp += str(new[i][j])
        result_90.append(tmp)
    
    # 180
    for i in range(N-1, -1, -1):
        tmp = ''
        for j in range(N-1, -1, -1):
            new[i][j] = board[i][j]
            tmp += str(new[i][j])
        result_180.append(tmp)
    
    # 270
    for i in range(N-1, -1, -1):
        tmp = ''
        for j in range(N):
            new[i][j] = board[j][i]
            tmp += str(new[i][j])
        result_270.append(tmp)
    
    print(f'#{tc}')
    for i in range(N):
        result = ''
        result += result_90[i] + ' '
        result += result_180[i] + ' '
        result += result_270[i]
        print(result)