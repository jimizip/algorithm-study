N, M = map(int, input().split())
arr = []
visited = [False] * (N+1)

def backtracking(num):
    if num == M: # 길이가 M인 수열을 완성한 경우
        print(' '.join(map(str, arr)))
        return
    for i in range(1, N+1):
        if not visited[i]:  # 아직 방문하지 않은 숫자만 선택
            visited[i] = True  # 현재 숫자를 방문 처리
            arr.append(i)  # 선택한 숫자를 수열에 추가
            backtracking(num+1)  # 다음 단계로 재귀 호출
            visited[i] = False  # 백트래킹: 방문 상태 복원
            arr.pop()  # 백트래킹: 수열에서 마지막 숫자 제거

backtracking(0)