for tc in range(1, 11):
    T = int(input())
    N, M = map(int, input().split())
    result = 1

    def z(n, m):
        global result
        if m == M:
            print(f'#{T} {result}')
            return
        else:
            result *= n
            z(n, m+1)

    z(N, 0)