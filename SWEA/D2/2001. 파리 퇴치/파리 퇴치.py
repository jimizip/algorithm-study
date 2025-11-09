T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            cnt_sum = 0 
            for k in range(i, i+M):
                cnt_row = board[k]
                for x in range(j, j+M):
                    cnt_sum += cnt_row[x]
            
            if cnt_sum > result:
                result = cnt_sum

    print(f'#{t} {result}')