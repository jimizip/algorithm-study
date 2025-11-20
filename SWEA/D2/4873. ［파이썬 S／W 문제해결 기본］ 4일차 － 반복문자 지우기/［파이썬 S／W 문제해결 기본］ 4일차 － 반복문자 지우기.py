T = int(input())
for tc in range(1, T+1):
    word = input().strip()
    i = 0
    while len(word) != i+1:
        if word[i] == word[i+1]:
            word = word[:i] + word[i+2:]
            i = 0
        else:
            i += 1

    if len(word) == 0:
        print(f'#{tc} {0}')
    else:
        print(f'#{tc} {len(word)}')