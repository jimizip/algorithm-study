def div(s, l, n):
    tmp = board[s][l]
    check = True
    for i in range(s, s+n):
        for j in range(l, l+n):
            if tmp != board[i][j]:
                check = False
                break
    if not check:
        half = n // 2
        div(s, l, half)
        div(s, l+half, half)
        div(s+half, l, half)
        div(s+half, l+half, half)
        return
    
    cnt[tmp] += 1
    return
    

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
cnt = {0:0, 1:0}
div(0, 0, N)
for i in cnt.values():
    print(i)