T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    arr[0][0] = 1
    for i in range(1, N):
        for j in range(N):
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

    print(f'#{t}')
    result = ''
    for i in range(N):
        print(*(arr[i][:i+1]))