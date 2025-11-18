T = int(input())
arr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for tc in range(1, T + 1):
    fm, fd, lm, ld = map(int, input().split())
    res = 0
    if fm == lm:
        res = (ld-fd)+1
    else:
        for i in range(fm, lm):
            res += arr[i-1]
        res += (ld-fd)+1
    print(f'#{tc} {res}')