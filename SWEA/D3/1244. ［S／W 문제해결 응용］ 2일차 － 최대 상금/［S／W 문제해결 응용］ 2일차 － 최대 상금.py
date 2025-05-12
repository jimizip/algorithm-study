def dfs(n, swap, num_lst, visited_v):
    num_len = len(num_lst)

    if n == swap:
        return int("".join(map(str, num_lst)))
    
    max_val = 0
    for i in range(num_len - 1):
        for j in range(i + 1, num_len):
            # 숫자 교환
            num_lst[i], num_lst[j] = num_lst[j], num_lst[i]
            check = int("".join(map(str, num_lst)))
            if (n, check) not in visited_v:
                max_val = max(max_val, dfs(n + 1, swap, num_lst, visited_v))
                visited_v.add((n, check))
            # 교환 횟수를 다 채운 후 원래 상태로 되돌리기 (백트래킹)
            num_lst[j], num_lst[i] = num_lst[i], num_lst[j]
    return max_val

T = int(input())  # 테스트 케이스 수 입력
for tc in range(1, T + 1):  # 각 테스트 케이스에 대해 반복
    num_str, swap_count = input().split()  # 숫자판 정보와 교환 횟수 입력
    num_lst = list(num_str)  # 숫자 문자열을 리스트로 변환 
    swap = int(swap_count)  # 교환 횟수를 정수로 변환
    visited_v = set()  # 방문한 상태를 저장하는 집합
    result = dfs(0, swap, num_lst, visited_v)
    print(f"#{tc} {result}")  # 결과 출력