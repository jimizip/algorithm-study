N = int(input())
arr = []

for i in range(1, N+1):
    tmp = []
    for j in str(i):
        tmp.append(j)
    if '3' in tmp or '6' in tmp or '9' in tmp:
        all = tmp.count('3') + tmp.count('6') + tmp.count('9')
        arr.append(all*'-')
    else:
        arr.append(str(i))
print(*arr)