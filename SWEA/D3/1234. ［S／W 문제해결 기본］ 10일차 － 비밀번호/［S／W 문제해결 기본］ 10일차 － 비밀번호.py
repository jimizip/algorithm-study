for tc in range(1, 11):
    N, num = input().split()
    arr = []
    tmp = []
    for i in num:
        arr.append(i)
    
    while True:
        a = len(arr)
        while len(arr) != 0:
            if len(arr) == 1:
                tmp.append(arr.pop(0))
                break
            if arr[0] != arr[1]:
                tmp.append(arr.pop(0))
            else:
                arr.pop(0)
                arr.pop(0)
        
        if len(tmp) == a:
            break
        else:
            arr = tmp
            tmp = []
    
    print(f'#{tc} {"".join(tmp)}')