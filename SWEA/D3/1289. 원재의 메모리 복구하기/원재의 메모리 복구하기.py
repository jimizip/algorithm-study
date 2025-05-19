T = int(input())
for tc in range(1, T+1):
    text = list(input())
    be = ['0']*len(text)
    cnt = 0
    for i in range(len(be)):
        if be[i] != text[i]:
            be[i:] = text[i]*len(be[i:]) # 덮어쓰기
            cnt += 1

    print(f'#{tc} {cnt}')