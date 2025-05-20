T = int(input())
for tc in range(1, T+1):
    N = int(input())
    price = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    result = [0]*(len(price))

    for i in range(len(price)):
        if N // price[i] != 0:
            result[i] = N // price[i]
            N %= price[i]

    print(f'#{tc}')
    print(' '.join(map(str, result)))