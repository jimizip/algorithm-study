T = int(input())
for t in range(1, T+1):
    word = input()
    first = word[0]
    word = word.replace(first, '-')
    result = 0
    cnt = 1

    while True:
        tmp = word.index('-', cnt)
        if word[:tmp] == word[tmp:tmp+tmp]:
            result = tmp
            break
        else:
            cnt += tmp

    print(f'#{t} {result}')