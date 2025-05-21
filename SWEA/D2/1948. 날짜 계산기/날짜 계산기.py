T = int(input())
for tc in range(1, 1+T):
    arr = list(map(int, input().split()))
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    result = (arr[3] - arr[1]) + 1

    if arr[2] - arr[0] != 0:
        for i in range(arr[0], arr[2]):
            result += days[i]
    
    print(f'#{tc} {result}')