T = int(input())
for t in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    flag = True

    for i in range(9):
        row_sum = 0
        col_sum = 0
        for j in range(9):
            row_sum += arr[i][j]
            col_sum += arr[j][i]

        if row_sum != 45 or col_sum != 45:
            flag = False
            break

    else:
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                sam_sum = 0
                for row in range(3):
                    for col in range(3):
                        sam_sum += arr[i+row][j+col]

                if sam_sum != 45:
                    flag = False
                    break

    if flag:
        print(f'#{t} {1}')
    else:
        print(f'#{t} {0}')