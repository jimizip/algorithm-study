import heapq

def dijkstra(graph, start, N):
    # 최단 거리 배열 초기화: 모든 노드까지의 거리를 무한대로 설정
    D = [float('inf')] * (N+1)
    D[start] = 0 # 시작 노드의 거리는 0
    # 우선순위 큐 (최소 힙) 초기화 및 시작 노드 추가
    q = []
    heapq.heappush(q, (0, start))  # (거리, 노드) 형식으로 저장
    
    while q:
        # 현재 가장 거리가 짧은 노드 선택
        dist, now = heapq.heappop(q)
        # 이미 처리된 노드인 경우 스킵
        # 현재 저장된 거리(D[now])가 힙에서 꺼낸 거리보다 작으면 더 이상 처리 필요 없음
        if D[now] < dist:
            continue
        # 현재 노드의 인접 노드 탐색
        for v, val in graph[now]:
            # 현재 노드를 거쳐서 가는 새로운 거리 계산
            cost = dist + val
            # 새로운 거리가 기존 거리보다 짧으면 갱신
            if cost < D[v]:
                D[v] = cost
                # 갱신된 거리로 큐에 삽입
                heapq.heappush(q, (cost, v))
    # 최종 최단 거리 배열 반환
    return D

N, M, X = map(int, input().split())
forward_graph = [[] for _ in range(N+1)]  # 정방향 그래프 (X에서 나가는 경로)
reverse_graph = [[] for _ in range(N+1)]  # 역방향 그래프 (X로 들어오는 경로)

for _ in range(M):
    a, b, t = map(int, input().split())
    forward_graph[a].append((b, t))  # 정방향: a -> b
    reverse_graph[b].append((a, t))  # 역방향: b -> a (X로 오는 경로 계산용)

# X에서 각 마을로 가는 최단 시간 (정방향 그래프)
return_time = dijkstra(forward_graph, X, N)

# 각 마을에서 X로 가는 최단 시간 (역방향 그래프)
go_time = dijkstra(reverse_graph, X, N)

max_time = 0
for i in range(1, N+1):
    max_time = max(max_time, return_time[i] + go_time[i])

print(max_time)