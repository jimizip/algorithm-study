for _ in range(1, 11):
    T = int(input())
    num = list(map(int, input().split()))

    while num[len(num)-1] != 0:
        for i in range(1, 6):
            num[0] -= i
            if num[0] < 0:
                num[0] = 0
            num.append(num.pop(0))
            if num[len(num)-1] == 0:
                break

    print(f"#{T} {' '.join(map(str, num))}")