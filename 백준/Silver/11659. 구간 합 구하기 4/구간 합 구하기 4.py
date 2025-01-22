import sys
input = sys.stdin.readline

N, M = map(int, input().split())

num = list(map(int, input().split()))
sum = [0]
temp = 0

# 누적합 배열
for i in num:
    temp += i
    sum.append(temp)

# 구간합
for _ in range(M):
    i, j = map(int, input().split())
    print(sum[j]-sum[i-1])