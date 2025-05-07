A, B = map(int, input().split())
arr = []
for i in range(1, B+1):
    if len(arr) >= B:
        break
    else:
        for j in range(i):
            arr.append(i)

print(sum(arr[A-1:B]))