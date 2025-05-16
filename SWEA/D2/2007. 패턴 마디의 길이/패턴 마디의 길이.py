T = int(input())
for tc in range(1, T+1):
    lis = input()
    result = 0
    tmp1 = []
    tmp2 = []

    for i in range(1, 11):
        tmp1 = lis[:i]
        tmp2 = lis[i:i*2]
        if tmp1 == tmp2:
            result = len(tmp1)
            break
    
    print(f'#{tc} {result}')