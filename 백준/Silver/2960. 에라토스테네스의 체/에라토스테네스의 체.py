N, K = map(int, input().split())
arr = []
result = []

for i in range(2, N+1):
    arr.append(i)

while len(arr) != 0:
    P = arr[0]
    result.append(P)
    arr.remove(P)
    for i in arr:
        if i % P == 0:
            result.append(i)
            arr.remove(i)


print(result[K-1])