for _ in range(1, 11):
    T = int(input())
    num = [list(map(int, input().split())) for _ in range(100)]

    row = 0
    for i in range(100):
        row = max(row, sum(num[i]))
    
    col = 0
    for i in range(100):
        tmp = 0
        for j in range(100):
            tmp += num[j][i]
        col = max(col, tmp)
    
    cross_front = 0
    for i in range(100):
        cross_front += num[i][i]
    
    cross_back = 0
    for i in range(100):
        cross_back += num[i][99-i]

    print(f'#{T} {max(row, col, cross_back, cross_front)}')