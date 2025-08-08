N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))

start = max(arr)  # 최소한 가장 큰 금액은 인출할 수 있어야 함
end = sum(arr)    # 모든 금액을 한 번에 인출하는 경우

answer = 0

while start <= end:
    mid = (start + end) // 2
    
    current_sum = 0
    cnt = 1
    for i in arr:
        if current_sum + i > mid:
            cnt += 1
            current_sum = i
        else:
            current_sum += i
    
    if cnt > M:
        start = mid + 1
    else:
        answer = mid
        end = mid - 1

print(answer)
