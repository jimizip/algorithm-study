from itertools import combinations

N , M = map(int, input().split())
arr = list(map(int, input().split()))
result = []

for i in combinations(arr, 3):
    if sum(i) <= M:
        result.append(sum(i))

print(max(result))