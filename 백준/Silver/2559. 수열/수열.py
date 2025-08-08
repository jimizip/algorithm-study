N, K = map(int, input().split())
arr = list(map(int, input().split()))
result = [sum(arr[:K]), ]

for i in range(N-K):
    result.append(result[i] - arr[i] + arr[i+K])

print(max(result))