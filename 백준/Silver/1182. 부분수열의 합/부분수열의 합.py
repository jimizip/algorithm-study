from itertools import combinations

N, S = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0
res = 0

for k in range(1, N+1):
    for i in combinations(nums, k):
        res = sum(i)
        if res == S:
            cnt += 1

print(cnt)