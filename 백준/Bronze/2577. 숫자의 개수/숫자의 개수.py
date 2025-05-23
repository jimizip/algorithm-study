A = int(input())
B = int(input())
C = int(input())

num = A * B * C

dic = {}
for i in str(num):
    if int(i) in dic:
        dic[int(i)] += 1
    else:
        dic[int(i)] = 1

for i in range(10):
    if i not in dic:
        print(0)
    else:
        print(dic[i])