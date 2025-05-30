def div(s, l, n):
    tmp = board[s][l]
    check = True
    for i in range(s, s+n):
        for j in range(l, l+n):
            if tmp != board[i][j]:
                check = False
                break
    if not check:
        next = n // 3
        div(s, l, next)
        div(s, l+next, next)
        div(s, l+(next*2), next)
        div(s+next, l, next)
        div(s+next, l+next, next)
        div(s+next, l+(next*2), next)
        div(s+(next*2), l, next)
        div(s+(next*2), l+next, next)
        div(s+(next*2), l+(next*2), next)
        return
    
    cnt[tmp] += 1
    return
    

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
cnt = {-1:0, 0:0, 1:0}
div(0, 0, N)
for i in cnt.values():
    print(i)