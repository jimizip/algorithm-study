# 입력
N = int(input())
P = list(map(int, input().split()))
P_add = [0] * N
result = 0

P.sort()

P_add[0] = P[0]
for i in range(1, N):
    P_add[i] = P_add[i-1] + P[i]

for i in range(N):
    result += P_add[i]

# 출력
print(result)