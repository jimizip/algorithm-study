for tc in range(1, 11):
    dump = int(input())
    boxs = list(map(int, input().split()))
    for i in range(dump):
        boxs.sort()
        if boxs[len(boxs)-1] - boxs[0] < 2:
            break
        boxs[0] += 1
        boxs[len(boxs)-1] -= 1
    boxs.sort()
    print(f'#{tc} {boxs[len(boxs)-1]-boxs[0]}')