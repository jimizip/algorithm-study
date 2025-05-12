for tc in range(1, 11):
    N = int(input())
    apt = list(map(int, input().split()))
    result = 0
    for i in range(2, len(apt)-2):
        tmp = max(max(apt[i+1:i+3]), max(apt[i-2:i]))
        if tmp > apt[i]:
            continue
        else:
            result += (apt[i]-tmp)
    print(f'#{tc} {result}')