def div(s, l, n):
    check = board[s][l]
    for i in range(s, s+n):
        for j in range(l, l+n):
            if check != board[i][j]:
                check = -1
                break
    if check == -1:
        half = n // 2
        print("(", end='')
        div(s, l, half)
        div(s, l+half, half)
        div(s+half, l, half)
        div(s+half, l+half, half)
        print(")", end='')
    elif check == 1:
        print(1, end='')
    else:
        print(0, end='')

N = int(input())
board = [list(map(int, input())) for _ in range(N)]
div(0, 0, N)