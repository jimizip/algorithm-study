T = int(input())

# i: 현재 탐색 중인 노드(정점)
# cnt: 현재까지 탐색한 경로의 길이 (노드의 수)
def dfs(i, cnt):
    global result

    if cnt > result:
        result = cnt

    visited[i] = True 
    # arr[i]는 노드 i의 인접 노드 리스트
    for j in arr[i]:
        # 만약 인접 노드 j를 아직 방문하지 않았다면
        if not visited[j]:
            # 인접 노드 j를 방문했다고 표시
            visited[j] = True
            # 인접 노드 j를 시작으로 하여 경로를 계속 탐색
            # 경로 길이는 1 증가
            dfs(j, cnt + 1)
            # 백트래킹
            # 노드 j로부터 시작하는 모든 경로 탐색이 끝났으면 "방문하지 않은 상태"로
            visited[j] = False
    visited[i] = False 

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [[] for _ in range(N + 1)]
    visited = [False] * (N + 1) 
    result = 0

    for _ in range(M):
        a, b = map(int, input().split())
        # 무방향 그래프이므로 양쪽 노드에 서로를 추가
        arr[a].append(b)
        arr[b].append(a)
    
    for i in range(1, N + 1):
        dfs(i, 1)

    print(f'#{tc} {result}')