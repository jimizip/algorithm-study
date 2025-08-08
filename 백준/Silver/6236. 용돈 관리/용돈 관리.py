N, M = map(int, input().split())
arr = []

for _ in range(N):
    arr.append(int(input()))

start = max(arr)
end = sum(arr)

while start <= end:
    mid = (start + end) // 2
    tmp = mid
    cnt = 1

    for i in arr:
        if tmp - i < 0 :
            cnt += 1
            tmp = mid
        tmp -= i
    
    if cnt > M:
        start = mid + 1
    else:
        end = mid - 1

print(mid)