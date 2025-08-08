N = int(input())
arr = list(map(int, input().split()))
arr.sort()

cnt = 0

for i in range(N):
    start = 0
    end = N-1
    goal = arr[i]
    while start < end:
        if arr[start] + arr[end] == goal:
            if i == start:
                start += 1
            elif i == end:
                end -= 1
            else:
                cnt += 1
                break
        elif arr[start] + arr[end] > goal:
            end -= 1
        elif arr[start] + arr[end] < goal:
            start += 1

print(cnt)