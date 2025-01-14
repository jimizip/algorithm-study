import sys
import heapq

input = sys.stdin.readline

# V: 정점의 개수, E: 간선의 개수
V, E = map(int, input().split())
# K: 시작 정점의 번호
K = int(input())
# 그래프를 인접 리스트로 표현
graph = [[] for _ in range(V+1)]
# 각 정점까지의 최단 거리를 저장할 리스트, 초기값은 무한대
distance = [float('inf')] * (V+1)

# 간선 정보 입력
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))  # u에서 v로 가는 가중치 w인 간선

def dijkstra(start):
    # 우선순위 큐 초기화: (거리, 정점) 튜플을 저장
    q = [(0, start)]
    distance[start] = 0

    while q:
        # 현재 최단 거리가 가장 짧은 노드 정보 꺼내기
        dist, now = heapq.heappop(q)
        
        # 이미 처리된 노드라면 무시
        if distance[now] < dist:
            continue
        
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for v, w in graph[now]:
            cost = dist + w
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(q, (cost, v))

# 다익스트라 알고리즘 수행
dijkstra(K)

# 각 정점으로의 최단 경로 값을 출력
for i in range(1, V+1):
    print(distance[i] if distance[i] != float('inf') else "INF")