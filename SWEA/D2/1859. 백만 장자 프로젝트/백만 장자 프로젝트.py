T = int(input())
for tc in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))
    result = 0
    max_num = 0

    for i in reversed(price):
        if i > max_num:
            max_num = i
        else:
            result += max_num - i
    
    print(f'#{tc} {result}')