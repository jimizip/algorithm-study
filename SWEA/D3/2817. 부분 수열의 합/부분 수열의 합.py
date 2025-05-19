T = int(input())

def dfs(i, result):
    global cnt
    if result == K:
        cnt += 1
        return
    if i == N:
        return
    dfs(i + 1, result + arr[i])
    dfs(i+1, result)

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    dfs(0, 0)
    print(f'#{tc} {cnt}')