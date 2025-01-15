import sys
import heapq
input = sys.stdin.readline

def find(a):
    while parent[a] != a:
        parent[a] = parent[parent[a]]  # 경로 압축
        a = parent[a]
    return a

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

# 입력
N, M = map(int, input().strip().split())
edges = []
parent = [0] * (N+1)

for i in range(N+1):
    parent[i] = i

# 데이터 저장
for _ in range(M):
    s, e, w = map(int, input().strip().split())
    heapq.heappush(edges, (w, s, e)) # 가중치 기준이기 때문에 맨 앞에 배치

useEdges = 0
result = 0

while edges and useEdges < N-1:
    w, s, e = heapq.heappop(edges)
    if find(s) != find(e):
        union(s, e)
        result += w
        useEdges += 1

# 출력
print(result)