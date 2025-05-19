T = int(input())
for tc in range(1, T+1):
    text = list(map(int, input()))
    be = [0]*(len(text))
    cnt = 0

    while text:
        if 1 in text:
            idx_1 = text.index(1)
            for i in range(idx_1, len(be)):
                be[i] = 1
            cnt += 1

        for i in range(len(text)):
            if text[0] == be[0]:
                text.pop(0)
                be.pop(0)
                
        if 0 in text:
            idx_0 = text.index(0)
            for i in range(idx_0, len(be)):
                be[i] = 0
            cnt += 1
    
    print(f'#{tc} {cnt}')