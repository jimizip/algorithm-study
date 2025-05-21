T = int(input())
for tc in range(1, 1 + T):
    H, W = map(int, input().split())
    board = [list(input()) for _ in range(H)] 
    
    car_char = ''
    car_pos = [-1, -1] 

    # 전차 초기 위치와 방향 찾기
    for r in range(H):
        for c in range(W):
            if board[r][c] == '^':
                car_char = '^'
                car_pos = [r, c]
                break
            elif board[r][c] == 'v':
                car_char = 'v'
                car_pos = [r, c]
                break
            elif board[r][c] == '<':
                car_char = '<'
                car_pos = [r, c]
                break
            elif board[r][c] == '>':
                car_char = '>'
                car_pos = [r, c]
                break
        if car_pos != [-1, -1]: # 전차를 찾았으면 외부 루프도 종료
            break
    
    user_cnt = int(input())
    user_input = input()

    # 사용자 입력력
    for i in range(user_cnt):
        cmd = user_input[i]
        
        current_r, current_c = car_pos[0], car_pos[1]

        if cmd == 'S': # Shoot
            shot_r, shot_c = current_r, current_c
            
            if car_char == '^':
                # 위로 발사
                while True:
                    shot_r -= 1
                    if shot_r < 0: # 맵 밖으로 나감
                        break
                    if board[shot_r][shot_c] == '*': # 강철 벽 만나면
                        board[shot_r][shot_c] = '.' # 파괴
                        break
                    elif board[shot_r][shot_c] == '#': # 강철 벽은 아무 일 없음
                        break
                    # 평지(.), 물(-)은 계속 진행
            elif car_char == 'v':
                # 아래로 발사
                while True:
                    shot_r += 1
                    if shot_r >= H:
                        break
                    if board[shot_r][shot_c] == '*':
                        board[shot_r][shot_c] = '.'
                        break
                    elif board[shot_r][shot_c] == '#':
                        break
            elif car_char == '<':
                # 왼쪽으로 발사
                while True:
                    shot_c -= 1
                    if shot_c < 0:
                        break
                    if board[shot_r][shot_c] == '*':
                        board[shot_r][shot_c] = '.'
                        break
                    elif board[shot_r][shot_c] == '#':
                        break
            elif car_char == '>':
                # 오른쪽으로 발사
                while True:
                    shot_c += 1
                    if shot_c >= W:
                        break
                    if board[shot_r][shot_c] == '*':
                        board[shot_r][shot_c] = '.'
                        break
                    elif board[shot_r][shot_c] == '#':
                        break
        
        # 이동 명령 (U, D, L, R)
        else:
            next_r, next_c = current_r, current_c # 다음 예상 위치
            
            if cmd == 'U':
                car_char = '^' # 방향 전환
                next_r -= 1
            elif cmd == 'D':
                car_char = 'v' # 방향 전환
                next_r += 1
            elif cmd == 'L':
                car_char = '<' # 방향 전환
                next_c -= 1
            elif cmd == 'R':
                car_char = '>' # 방향 전환
                next_c += 1
            
            # 현재 위치의 전차를 평지로 만듦
            board[current_r][current_c] = '.' 
            
            # 다음 위치가 맵 범위 내이고 평지(.)인지 확인
            if 0 <= next_r < H and 0 <= next_c < W and board[next_r][next_c] == '.':
                # 이동 가능하면 전차 위치 업데이트
                car_pos = [next_r, next_c]
            else:
                # 이동 불가능하면 원래 위치로 (방향만 바뀐 상태 유지)
                pass

            # 최종 전차 위치에 전차 모양 업데이트
            board[car_pos[0]][car_pos[1]] = car_char

    print(f"#{tc} ", end="")
    for r_idx in range(H):
        print("".join(board[r_idx]))