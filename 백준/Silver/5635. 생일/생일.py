n = int(input())

result = []

for _ in range(n):
    name, dd, mm, yyyy = input().split()
    result.append((name, int(yyyy), int(mm), int(dd)))

old = min(result, key=lambda x: (x[1], x[2],x[3]))
young = max(result, key=lambda x: (x[1], x[2],x[3]))

print(young[0])
print(old[0])