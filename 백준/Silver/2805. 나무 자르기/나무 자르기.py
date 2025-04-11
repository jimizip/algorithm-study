N, M = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree)

result = 0
while start <= end:
    mid = (start + end) // 2

    total = 0
    for i in tree:
        if i > mid:
            total += i - mid
    
    if total >= M:
        result = mid
        start = mid + 1
    else:
        end = mid - 1
    
print(result)