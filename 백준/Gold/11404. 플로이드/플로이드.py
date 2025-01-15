import sys
input = sys.stdin.readline

# 입력
N = int(input())
M = int(input())
distance = [[sys.maxsize for j in range(N+1)] for i in range(N+1)]

# 시작 도시와 도착 도시가 같은 경우는 없다
for i in range(1, N+1):
    distance[i][i] = 0

# 데이터 저장
for _ in range(M):
    start, end, time = map(int, input().split())
    if distance[start][end] > time:
        distance[start][end] = time

# 플로이드워셜 알고리즘 수행 (모든 ~ 최단거리)
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if distance[i][j] > distance[i][k] + distance[k][j]:
                distance[i][j] = distance[i][k] + distance[k][j]

# 출력
for i in range(1, N+1):
    for j in range(1, N+1):
        if distance[i][j] == sys.maxsize:
            print(0, end=' ')
        else:
            print(distance[i][j], end=' ')
    print()