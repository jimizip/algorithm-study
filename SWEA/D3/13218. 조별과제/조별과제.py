T = int(input())
for tc in range(1, T+1):
    N = int(input())
    if N < 3:
        result = 0
    else:
        result = N // 3

    print(f'#{tc} {result}')