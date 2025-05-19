for tc in range(1, 11):
    T = int(input())
    find = input()
    text = input()
    cnt = 0
    
    while text.count(find[0]) != 0:
        first = text.index(find[0])
        tmp = text[first:first+len(find)]
        if tmp != find:
            text = text[first+1:]
        else:
            cnt += 1
            text = text[first+1:]
    
    print(f'#{T} {cnt}')