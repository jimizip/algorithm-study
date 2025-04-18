import sys
input = sys.stdin.readline

M = int(input())
S = set()

for _ in range(M):
    arr = list(input().split())

    if arr[0] == 'add':
        S.add(int(arr[1]))
    elif arr[0] == 'remove':
        # 원소 삭제 시 에러X
        S.discard(int(arr[1]))
    elif arr[0] == 'check':
        if int(arr[1]) in S:
            print(1)
        else:
            print(0)
    elif arr[0] == 'toggle':
        if int(arr[1]) in S:
            S.discard(int(arr[1]))
        else:
            S.add(int(arr[1]))
    elif arr[0] == 'all':
        S = set([i for i in range(1,21)])
    else:
        S = set()