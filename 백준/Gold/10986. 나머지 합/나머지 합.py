import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

S = [0] * N
C = [0] * M
result = 0

S[0] = A[0]
for i in range(1, N):
    S[i] = S[i-1] + A[i]

for i in range(N):
    remainder = S[i] % M
    if remainder == 0:
        result += 1
    C[remainder] += 1

for i in range(M):
    if C[i] > 1:
        result += ((C[i] * (C[i]-1)) // 2)
    
print(result)
