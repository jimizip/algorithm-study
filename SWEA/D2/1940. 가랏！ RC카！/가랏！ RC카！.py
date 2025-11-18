T = int(input())
for tc in range(1, T + 1):
    n = int(input())

    v = 0  # 현재 속도 (m/s)
    dist = 0  # 총 이동거리 (m)

    for _ in range(n):
        cmd = list(map(int, input().split()))

        if cmd[0] == 1:  # 가속
            v += cmd[1]  # 속도 = 현재속도 + 가속도
        elif cmd[0] == 2:  # 감속
            v -= cmd[1]  # 속도 = 현재속도 - 가속도
            if v < 0:  # 속도가 음수가 되면 0으로 설정
                v = 0
        # cmd[0] == 0이면 속도 유지 (아무것도 안함)

        dist += v  # 1초 동안 현재 속도만큼 이동

    print(f"#{tc} {dist}")
