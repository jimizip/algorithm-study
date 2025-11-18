T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    res = []
    for i in range(N-M+1):
        res.append(sum(arr[i:i+M]))
    print(f'#{tc}', (max(res)-min(res)))