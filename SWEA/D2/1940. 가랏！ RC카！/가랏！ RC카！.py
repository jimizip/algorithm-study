T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    result = 0
    s = 0
    for _ in range(N):
        cmd = list(map(int, input().split()))
        if cmd[0] == 1:
            s += cmd[1]
        elif cmd[0] == 2:
            s -= cmd[1]
            if s < 0:
                s = 0
        result += s
    
    print(f'#{tc} {result}')