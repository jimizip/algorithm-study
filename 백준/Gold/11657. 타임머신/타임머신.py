import sys
input = sys.stdin.readline

# 입력
N, M = map(int, input().split())
edges = []
distance = [sys.maxsize] * (N+1)

# 데이터 저장
for _ in range(M):
    start, end, time = map(int, input().split())
    edges.append((start, end, time))

# 출발 노드 0으로 초기화
distance[1] = 0

for _ in range(N-1):
    for start, end, time in edges:
        # 출발 노드가 무한대가 아니고 종료 노드값 > 출발 노드값 + 가중치
        if distance[start] != sys.maxsize and distance[end] > distance[start] + time:
            distance[end] = distance[start] + time
    
mCycle = False

# 음수 사이클 존재 여부
for start, end, time in edges:
    if distance[start] != sys.maxsize and distance[end] > distance[start] + time:
            mCycle = True

if not mCycle:
    for i in range(2, N+1):
        if distance[i] != sys.maxsize:
            print(distance[i])
        else:
            print(-1)
else:
    print(-1)