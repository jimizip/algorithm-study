N, M = map(int, input().split())
arr = dict()
result = []

for i in range(N):
    name1 = input()
    arr[name1] = i

for _ in range(M):
    name = input()
    if name in arr:
        result.append(name)

result.sort()
print(len(result))
for i in result:
    print(i)