T = int(input())
for tc in range(1, T+1):
    N = int(input())
    set_list = set()
    i = 1
    t = N
    while len(set_list) != 10:
        t= str(i*N)
        for j in t:
            set_list.add(int(j))
        i += 1
    
    print(f'#{tc} {int(t)}')