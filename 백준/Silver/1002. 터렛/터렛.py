import math

T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = list(map(int, input().split()))

    # 두 원 중심 사이의 거리
    dis = math.sqrt((x1-x2)**2 + (y1-y2)**2)

    # 두 원의 중심이 같을 경우
    if dis == 0:
        # 두 원의 크기가 같아 겹치는 겅우
        if r1 == r2:
            print(-1)
        # 내부에 포함되어 만나지 않는 경우
        else:
            print(0)
    # 두 원의 중심이 다를 경우우
    else: 
        # 외접이거나 내접인 경우우
        if r1+r2 == dis or abs(r2-r1) == dis:
            print(1)
        # 접점이 2개인 경우우
        elif ((abs(r1-r2) < dis) and (dis < r1+r2)):
            print(2)
        # 이 외는 모두 접점 X
        else:
            print(0)