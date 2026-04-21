from itertools import combinations
arr = []
result = []
for _ in range(9):
    arr.append(int(input()))

for i in combinations(arr, 7):
    if sum(i) == 100:
        result = i
        break

for i in result:
    print(i)