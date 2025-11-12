import math

T = int(input())
for t in range(1, T+1):
    arr = list(map(int, input().split()))
    arr.sort()
    result = round((sum(arr[1:9]) / 8))
    print(f'#{t} {result}')
