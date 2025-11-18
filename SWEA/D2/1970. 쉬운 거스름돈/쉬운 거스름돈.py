T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    res = []

    for i in arr:
        res.append(N//i)
        N = N % i

    print(f'#{t}')
    print(*res)