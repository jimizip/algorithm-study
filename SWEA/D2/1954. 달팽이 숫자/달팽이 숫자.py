def snails(n):
    snail = [[0] * n for _ in range(n)]

    dx = [0, 1, 0, -1] # 행 변화량: 오른쪽(0), 아래(1), 왼쪽(0), 위(-1)
    dy = [1, 0, -1, 0] # 열 변화량: 오른쪽(1), 아래(0), 왼쪽(-1), 위(0)

    # x, y: 현재 숫자를 채울 위치의 행(x)과 열(y) 인덱스. 처음 시작은 (0, 0)
    # d: 현재 이동 방향을 나타내는 인덱스 (dx, dy 배열의 인덱스).
    #    d의 초기값 0에 따라 첫 방향이 결정
    #    d=0일 때 (dx[0], dy[0]) = (0, 1) 이므로 첫 방향은 '오른쪽'
    x, y, d = 0, 0, 0 

    for i in range(1, n * n + 1):
        snail[x][y] = i
        
        nx = x + dx[d]  # 다음 행 위치
        ny = y + dy[d]  # 다음 열 위치
 
        # 다음 위치 (nx, ny)가 배열의 범위를 벗어나거나,
        # 또는 다음 위치에 이미 다른 숫자가 채워져 있다면 (snail[nx][ny] != 0),
        if nx < 0 or nx >= n or ny < 0 or ny >= n or snail[nx][ny] != 0:
            # (d + 1) % 4: 현재 방향 d에서 시계방향으로 90도 회전한 다음 방향
            # 0(오른쪽) -> 1(아래) -> 2(왼쪽) -> 3(위) -> 0(오른쪽) ...
            d = (d + 1) % 4
            # 바뀐 방향으로 다시 다음 위치를 계산
            nx = x + dx[d]
            ny = y + dy[d]
            
        # 현재 위치 (x, y)를 다음 위치 (nx, ny)로 업데이트
        x, y = nx, ny

    return snail
         
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    result = snails(N)
    print(f'#{tc}')
    for i in result:
        print(*i)