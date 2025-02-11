import sys
input = sys.stdin.readline

N, M = map(int, input().split())
mon_dict = {}

# 두 가지 동시 매핑
for i in range(1, N+1):
    a = input().strip()
    mon_dict[i] = a
    mon_dict[a] = i

for i in range(M):
    q = input().strip()
    if q.isdigit():
        print(mon_dict[int(q)])
    else:
        print(mon_dict[q])