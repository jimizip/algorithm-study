for tc in range(1, 11):
    N = int(input())
    num = [list(input()) for _ in range(8)]
    cnt = 0

    for i in range(8):
        for j in range(8-N+1):
            tmp = num[i][j:j+N]
            if tmp == tmp[::-1]:
                cnt+=1
    
    for i in range(8):
        for j in range(8-N+1):
            tmp = []
            for k in range(N):
                tmp.append(num[j+k][i])
            if tmp == tmp[::-1]:
                cnt+=1

    print(f"#{tc} {cnt}")