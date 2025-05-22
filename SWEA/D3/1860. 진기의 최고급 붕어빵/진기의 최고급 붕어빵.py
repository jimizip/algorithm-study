T = int(input())
for tc in range(1, 1+T):
    N, M, K = map(int, input().split())
    arr = sorted(list(map(int, input().split())))
    flag = False
    bread = 0
    j = 0
    for i in range(1, arr[len(arr)-1]+1):
        if j == N:
            break

        if i % M == 0:
            bread += K
        
        if arr[j] == i:
            if bread - 1 < 0:
                flag = False
                break
            else:
                flag = True
                j += 1
                bread -= 1
    
    if flag == True:
        print(f'#{tc} Possible')
    else:
        print(f'#{tc} Impossible')