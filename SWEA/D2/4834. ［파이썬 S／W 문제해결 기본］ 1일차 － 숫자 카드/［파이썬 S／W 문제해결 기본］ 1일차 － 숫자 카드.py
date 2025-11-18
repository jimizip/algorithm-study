T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    cards = input()

    cnt = {}

    for c in cards:
        if int(c) in cnt:
            cnt[int(c)] += 1
        else:
            cnt[int(c)] = 1

    max_cnt = max(cnt.values())
    max_num = 0

    for i in range(9, -1, -1):
        if i in cnt:
            if cnt[i] >= max_cnt and i >= max_num:
                max_num = i
                break

    print(f"#{tc} {max_num} {max_cnt}")
