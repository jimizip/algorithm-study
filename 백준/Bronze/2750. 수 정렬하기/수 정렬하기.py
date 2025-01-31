N = int(input())
num_list = []
for _ in range(N):
    num = int(input())
    num_list.append(num)

num_list.sort()
print(*num_list)