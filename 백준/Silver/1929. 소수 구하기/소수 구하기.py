import math

M, N = map(int, input().split())
num_list = []
result = 0

for i in range(M, N+1):
    if i == 1:
        continue
    for j in range(2, int(math.sqrt(i))+1):
        if i % j == 0:
            break
    else:
        print(i)