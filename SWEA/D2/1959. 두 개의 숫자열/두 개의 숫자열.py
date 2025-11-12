T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    result = 0
    cnt = abs(N-M) + 1

    if N > M:
        long_arr = A
        short_arr = B
    else:
        long_arr = B
        short_arr = A

    for i in range(cnt):
        sum_tmp = 0
        tmp = long_arr[i:i+len(short_arr)]
        for j in range(len(short_arr)):
            sum_tmp += (short_arr[j]*tmp[j])
        result = max(result, sum_tmp)

    print(f'#{t} {result}')