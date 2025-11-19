def binary_search(p, target):
    l, r = 1, p
    cnt = 0

    while l <= r:
        cnt += 1
        c = int((l + r) / 2)

        if c == target:
            return cnt
        elif c < target:
            l = c 
        else:
            r = c

    return cnt


T = int(input())
for tc in range(1, T + 1):
    p, pa, pb = map(int, input().split())

    cnt_a = binary_search(p, pa)
    cnt_b = binary_search(p, pb)

    if cnt_a < cnt_b:
        result = 'A'
    elif cnt_a > cnt_b:
        result = 'B'
    else:
        result = 0

    print(f"#{tc} {result}")