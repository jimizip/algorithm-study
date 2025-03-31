import sys
input = sys.stdin.readline
N = int(input())
arr = []

for _ in range(N):
    cmd = list(input().split())
    if cmd[0] == 'push':
        arr.append(cmd[1])
    elif cmd[0] == 'pop':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[0])
            arr.remove(arr[0])
    elif cmd[0] == 'size':
        print(len(arr))
    elif cmd[0] == 'empty':
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'front':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[0])
    else:
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[len(arr)-1])