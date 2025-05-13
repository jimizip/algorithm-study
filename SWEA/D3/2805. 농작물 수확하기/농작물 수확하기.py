T = int(input())
for tc in range(1, T+1):
    N = int(input())
    price_list = [list(map(int, input())) for _ in range(N)]
    result = 0
    mid = N // 2
    for i in range(N):
        if i == 0 or i == (N-1):
            result += price_list[i][mid]
        elif i == mid:
            result += sum(price_list[i])
        else:
            for j in range(abs(mid-i), (N-abs(mid-i))):
                result += price_list[i][j]
    
    print(f'#{tc} {result}')