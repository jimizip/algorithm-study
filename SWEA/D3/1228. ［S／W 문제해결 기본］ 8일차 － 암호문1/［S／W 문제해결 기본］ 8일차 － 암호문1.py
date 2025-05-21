for tc in range(1, 11):
    N = int(input())
    ori = input().split()
    In_cnt = int(input())
    In_arr = input().split()

    for i in range(In_cnt):
        I = In_arr.index('I')
        x = int(In_arr[I+1])
        y = int(In_arr[I+2])
        tmp = In_arr[I+3:I+3+y]

        for j in range(x, x+y):
            ori.insert(j, tmp[0])
            tmp.pop(0)
        
        In_arr.remove(In_arr[I])
    
    print(f'#{tc} {" ".join(map(str, ori[:10]))}')