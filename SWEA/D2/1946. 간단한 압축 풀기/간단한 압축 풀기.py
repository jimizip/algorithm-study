T = int(input())
for tc in range(1, T + 1):
    print(f'#{tc}')
    N = int(input())
    res = ''
    for _ in range(N):
        word, idx = input().split()
        for _ in range(int(idx)):
            res += word
            if len(res) == 10:
                print(res)
                res = ''
    print(res)