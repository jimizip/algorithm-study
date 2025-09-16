from collections import deque

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

x, y, size = 0, 0, 2

# 초기 상어의 위치(값이 9인 곳)
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            x = i
            y = j


# 먹을 물고기를 찾는 함수 (BFS 사용)
def bfs(x, y, shark_size):
    # 거리 저장 list
    distance = [[0] * N for _ in range(N)]
    # 방문 확인 list
    visited = [[0] * N for _ in range(N)]

    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    # 먹을 수 있는 물고기들의 정보를 저장할 리스트
    temp = []

    while q:
        cur_x, cur_y = q.popleft()

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                # 상어가 지나갈 수 있는 위치인가?
                if graph[nx][ny] <= shark_size:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    # 거리를 1 증가시켜 저장 (현재 칸까지의 거리 + 1)
                    distance[nx][ny] = distance[cur_x][cur_y] + 1

                    # 상어가 먹을 수 있는 물고기가 있는가?
                    if graph[nx][ny] < shark_size and graph[nx][ny] != 0:
                        temp.append((nx, ny, distance[nx][ny]))

    # 1. 거리(x[2]) 오름차순
    # 2. 행(x[0]) 오름차순
    # 3. 열(x[1]) 오름차순
    # key에 -를 붙여 정렬하면 내림차순이 되는데, pop()으로 마지막 원소를 꺼낼 것이므로
    # 사실상 (거리, 행, 열) 순서로 오름차순 정렬한 것과 같은 효과 (거리가 짦은거, 가장 위에 있는거, 가장 왼쪽에 있는거)
    return sorted(temp, key=lambda x: (-x[2], -x[0], -x[1]))


cnt = 0
result = 0

while True:
    shark = bfs(x, y, size)

    if len(shark) == 0:
        break

    # 정렬된 리스트에서 가장 우선순위가 높은 물고기를 꺼냄
    nx, ny, dist = shark.pop()

    # 물고기를 먹으러 이동한 거리를 총 시간에 더해
    result += dist

    # 상어가 있던 원래 위치와 물고기를 먹은 위치를 빈칸(0)으로
    graph[x][y], graph[nx][ny] = 0, 0

    # 상어의 위치를 물고기를 먹은 위치로 업데이트
    x, y = nx, ny

    # 물고기를 한 마리 먹었으므로 cnt를 1 증가
    cnt += 1

    # 먹은 물고기 수가 상어의 크기와 같아지면 상어가 성장
    if cnt == size:
        size += 1
        cnt = 0  # 먹은 물고기 수 초기화

print(result)