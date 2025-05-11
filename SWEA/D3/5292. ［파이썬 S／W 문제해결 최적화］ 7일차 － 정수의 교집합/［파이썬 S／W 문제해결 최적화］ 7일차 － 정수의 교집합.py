T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    n = set(map(int, input().split()))
    m = set(map(int, input().split()))
    cnt = 0

    for i in n:
        if i in m:
            cnt += 1

    print(f'#{tc} {cnt}') 