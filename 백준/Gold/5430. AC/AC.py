from collections import deque

T = int(input())
for _ in range(T):
    p = input()
    n = int(input())
    arr_str = input()

    if n == 0:
        # nums = deque() # 이렇게 해도 되고, 아래처럼 파싱 후 비어있는지 확인해도 됨
        if 'D' in p:
            print("error")
        else:
            print("[]")
        continue

    # 문자열 파싱하여 deque 생성
    # 예: "[1,2,3]" -> deque([1, 2, 3])
    # strip으로 '['와 ']' 제거 후 split(',')
    nums_str_list = arr_str[1:-1].split(',')
    if nums_str_list == ['']: # 빈 문자열 원소 하나만 있는 경우 (n=0인데 arr_str이 "[]"인 경우 처리)
        nums = deque()
    else:
        nums = deque(map(int, nums_str_list))

    is_reversed = False
    error_occurred = False

    for command in p:
        if command == 'R':
            is_reversed = not is_reversed
        elif command == 'D':
            if not nums: # deque가 비어있으면
                error_occurred = True
                break
            if is_reversed:
                nums.pop() # 뒤집힌 상태에서는 오른쪽(pop)이 앞
            else:
                nums.popleft() # 정방향 상태에서는 왼쪽(popleft)이 앞

    if error_occurred:
        print("error")
    else:
        if is_reversed:
            nums.reverse() # 최종 출력 전에 딱 한 번만 reverse (필요하다면)
        print("[" + ",".join(map(str, nums)) + "]")