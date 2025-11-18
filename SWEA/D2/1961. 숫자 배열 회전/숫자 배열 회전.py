T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    
    # 90도 회전 함수
    def rotate(a):
        # zip(*a[::-1]): a를 상하반전([::-1])한 후 전치행렬(*연산)
        # [::-1]은 슬라이싱으로 역순 배열
        # *는 언패킹, zip은 행<->열 전환(전치행렬)
        return [list(x) for x in zip(*a[::-1])]
    
    # 각도별 회전
    r90 = rotate(arr)           # 90도
    r180 = rotate(r90)          # 180도 (90도를 한번 더 회전)
    r270 = rotate(r180)         # 270도 (90도를 두번 더 회전)
    
    print(f"#{tc}")
    # 각 행마다 세 회전 결과를 공백으로 구분하여 출력
    for i in range(n):
        # join: 리스트를 문자열로 결합
        # map(str, list): 숫자 리스트를 문자열 리스트로 변환
        s90 = ''.join(map(str, r90[i]))
        s180 = ''.join(map(str, r180[i]))
        s270 = ''.join(map(str, r270[i]))
        print(s90, s180, s270)
