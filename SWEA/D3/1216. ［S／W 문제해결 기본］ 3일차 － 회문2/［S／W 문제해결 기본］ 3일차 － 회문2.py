for _ in range(1, 11):
    T = int(input())
    arr = [list(input()) for _ in range(100)]
    new_arr = list(map(list, zip(*arr)))
    result = 0

    for i in range(100):
        tmp = []
        for j in range(100):
            for k in range(j, 101):
                tmp = arr[i][j:k]
                tmp_len = len(tmp)
                if tmp == tmp[::-1]:
                    if result < tmp_len:
                        result = tmp_len
    
    for i in range(100):
        tmp = []
        for j in range(100):
            for k in range(j, 101):
                tmp = new_arr[i][j:k]
                tmp_len = len(tmp)
                if tmp == tmp[::-1]:
                    if result < tmp_len:
                        result = tmp_len

    print(f'#{T} {result}')