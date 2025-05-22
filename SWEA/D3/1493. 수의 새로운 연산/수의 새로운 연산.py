T = int(input()) 
for tc in range(1, T + 1):
    p, q = map(int, input().split())
 
    def get_xy(n):
        s = 0     # 그 전 대각선 그룹((line-1)번째 대각선)까지의 총 숫자 개수를 저장할 변수
        line = 0  # 현재 대각선 그룹의 번호

        # n이 몇 번째 대각선 라인에 속하는지 찾는 루프
        while s < n:
            # 다음 대각선 라인으로 이동
            line += 1  # 대각선 번호를 1 증가 (1번째, 2번째, 3번째 라인...)
            s += line  # 현재 line번째 대각선에 있는 숫자의 개수(line개)를 s에 더함.
                    # 루프가 끝나면 s는 "n이 속한 line번째 대각선까지의 모든 숫자의 총 개수"가 됨.
                    # 또는 "n이 속한 line번째 대각선의 마지막 숫자의 값"과 동일.

        # 루프 종료 후:
        # line: 숫자 n이 속한 대각선 라인의 번호.
        # s:    line번째 대각선까지의 모든 숫자의 총 개수 (즉, line번째 대각선의 마지막 숫자의 값).

        # offset 계산:
        # (s - line): line번째 대각선을 제외한, (line-1)번째 대각선까지의 총 숫자 개수.
        #             이것은 line번째 대각선의 "시작 숫자 - 1"과 같습니다.
        # n - (s - line): line번째 대각선에서 n이 몇 번째 위치에 있는지 (1부터 시작하는 위치).
        # offset = n - (s - line) - 1: line번째 대각선에서 n이 몇 번째 위치에 있는지 (0부터 시작하는 인덱스).
        #                               0이면 해당 라인의 첫 번째 숫자, 1이면 두 번째 숫자, ...
        offset = n - (s - line) - 1

        # 좌표 계산:
        # line번째 대각선에 있는 좌표들은 (1, line), (2, line-1), ..., (line, 1) 순서
        # x 좌표는 1부터 시작해서 offset만큼 증가
        x = 1 + offset
        # y 좌표는 line에서 시작해서 offset만큼 감소
        y = line - offset
        
        return x, y

 
    # 함수 get_num(x, y): 2차원 좌표 (x, y)를 1차원 숫자 n으로 변환합니다.
    def get_num(x, y):
        # line: (x, y) 좌표가 속한 대각선 라인의 번호
        # (x,y)가 속한 대각선은 모든 좌표의 합이 x+y 임. 이 대각선은 (x+y-1)번째 대각선.
        line = x + y - 1
        
        # start: (line-1)번째 대각선 라인까지의 총 숫자 개수 + 1
        # 즉, line번째 대각선 라인의 첫 번째 숫자의 값
        # 1부터 (line-1)까지의 합은 (line-1) * line // 2 -> 등차수열 합 공식식
        start = line * (line - 1) // 2 + 1
        
        # 해당 대각선 라인에서 x좌표만큼 더 진행한 값이 최종 숫자.
        # 이 대각선은 (1, line), (2, line-1), ..., (x, y), ..., (line, 1) 순서.
        # x좌표는 1부터 시작하므로, (x-1)만큼의 오프셋을 가짐.
        return start + x - 1
 
    x1, y1 = get_xy(p)
    x2, y2 = get_xy(q)
    
    new_x = x1 + x2
    new_y = y1 + y2

    result = get_num(new_x, new_y)
 
    print(f"#{tc} {result}")