T = int(input())
for t in range(1, T+1):
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    N = int(input())
    K = 0
    tmp = 0
    while len(num) != 0:
        K += 1
        tmp = str(N*K)
        if len(tmp) > 1:
            for i in tmp:
                if i in num:
                    num.remove(i)
        else:
            if tmp in num:
                num.remove(tmp)
    print(f'#{t} {tmp}')