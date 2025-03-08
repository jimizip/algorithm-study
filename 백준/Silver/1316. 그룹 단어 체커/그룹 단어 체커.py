import sys

input = sys.stdin.readline



n = int(input())
cnt = n

for i in range(n):
    group = []
    str = list(input().strip())
    for j in range(len(str)):
        if str[j] not in group:
            group.append(str[j])
            check = str[j]
            continue
        if check == str[j]:
            continue
        if str[j] in group:
            cnt -= 1
            break


print(cnt)
         

