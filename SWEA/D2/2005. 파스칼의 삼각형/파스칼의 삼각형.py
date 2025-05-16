T = int(input())
for tc in range(1, T+1):
    N = int(input())
    d = [[0]*N for _ in range(N+1)]
    print(f'#{tc}')
    for i in range(1, N+1):
        d[i][0] = 1
    
    for n in range(2, N+1):
        for j in range(1, i):
            d[n][j] = d[n-1][j-1] + d[n-1][j]

    for i in range(1, N+1):
        print(*d[i][:i])