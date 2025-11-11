T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    tmp = 0

    # 가로 체크
    for i in range(N):
        tmp = 0
        for j in range(N):
            if arr[i][j] == 1:
                tmp += 1
            if arr[i][j] == 0 or j == N-1:
                if tmp == K:
                    cnt += 1
                tmp = 0


    # 세로 체크
    for i in range(N):
        tmp = 0
        for j in range(N):
            if arr[j][i] == 1:
                tmp += 1
            if arr[j][i] == 0 or j == N - 1:
                if tmp == K:
                    cnt += 1
                tmp = 0

    print(f'#{t} {cnt}')