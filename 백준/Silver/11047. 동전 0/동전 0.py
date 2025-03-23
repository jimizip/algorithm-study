N, K = map(int, input().split())
num_list = []
result = 0

for _ in range(N):
    a = int(input())
    if a > K:
        continue
    else:
        num_list.append(a)

while K != 0:
    if K >= num_list[len(num_list)-1]:
        result += K // num_list[len(num_list)-1]
        K = K % num_list[len(num_list)-1]
        num_list.pop()
    else:
        num_list.pop()

print(result)