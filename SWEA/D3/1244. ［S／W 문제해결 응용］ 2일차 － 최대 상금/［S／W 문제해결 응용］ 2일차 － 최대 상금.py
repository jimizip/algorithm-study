def dfs(n, swap, num_lst, visited_v):
    """
    Args:
        n (int): 현재 swap 횟수.
        swap (int): 총 swap 횟수.
        num_lst (list): 숫자 문자열을 리스트로 변환한 것.
        visited_v (set): 방문 여부를 저장하는 집합. (n, 현재 숫자 리스트의 정수 표현) 형태의 튜플을 저장.

    Returns:
        int: 만들 수 있는 최댓값.
    """
    num_len = len(num_lst)

    # swap 횟수를 모두 사용했다면, 현재 숫자 리스트를 정수로 변환하여 반환
    if n == swap:
        return int("".join(map(str, num_lst)))
    
    max_val = 0  # 현재 상태에서 만들 수 있는 최댓값을 저장할 변수 초기화

    # 모든 가능한 swap 조합에 대해 반복
    for i in range(num_len - 1):
        for j in range(i + 1, num_len):
            # 숫자 교환
            num_lst[i], num_lst[j] = num_lst[j], num_lst[i]
            
            # 현재 숫자 리스트를 정수로 변환
            check = int("".join(map(str, num_lst)))
            
            # (현재 swap 횟수, 현재 숫자) 조합이 방문한 적 없는 경우
            if (n, check) not in visited_v:
                # 다음 swap 횟수로 DFS 탐색, 반환된 값과 max_val 비교 후 갱신
                max_val = max(max_val, dfs(n + 1, swap, num_lst, visited_v))
                # 방문 처리
                visited_v.add((n, check))
                
            # 교환 횟수를 다 채운 후 원래 상태로 되돌리기 (백트래킹)
            num_lst[j], num_lst[i] = num_lst[i], num_lst[j]
            
    return max_val  # 만들 수 있는 최댓값 반환

T = int(input())  # 테스트 케이스 수 입력
for tc in range(1, T + 1):  # 각 테스트 케이스에 대해 반복
    num_str, swap_count = input().split()  # 숫자판 정보와 교환 횟수 입력
    num_lst = list(num_str)  # 숫자 문자열을 리스트로 변환 
    swap = int(swap_count)  # 교환 횟수를 정수로 변환
    visited_v = set()  # 방문한 상태를 저장하는 집합
    result = dfs(0, swap, num_lst, visited_v)  # DFS를 시작하여 결과를 얻음
    print(f"#{tc} {result}")  # 결과 출력