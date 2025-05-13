T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    nums = []
    for _ in range(N):
        row = list(map(int, input()))
        if 1 in row:
            nums.append(row)

    key_nums = []
    total_sum = 0
    
    for num in nums:
        result = []
        ans = []
        
        # 뒤에서부터 1을 찾아 암호 코드 시작점 찾기
        start_index = -1
        for i in range(M - 1, -1, -1):
            if num[i] == 1:
                start_index = i
                break
        
        if start_index == -1:
            print(f'#{tc} {0}')
            continue
            
        # 56개의 숫자 추출
        for i in range(start_index, start_index - 56, -1):
            if i < 0:
                ans = []
                break
            ans.append(num[i])

        if len(ans) != 56:
            continue

        ans.reverse()

        # 7자리씩 끊어서 숫자 해석
        key_nums = []
        for i in range(0, 56, 7):
            result_tmp = ans[i:i + 7]
            
            # 각 7자리 코드에 따른 숫자 판별
            if result_tmp == [0, 0, 0, 1, 1, 0, 1]:
                key_nums.append(0)
            elif result_tmp == [0, 0, 1, 1, 0, 0, 1]:
                key_nums.append(1)
            elif result_tmp == [0, 0, 1, 0, 0, 1, 1]:
                key_nums.append(2)
            elif result_tmp == [0, 1, 1, 1, 1, 0, 1]:
                key_nums.append(3)
            elif result_tmp == [0, 1, 0, 0, 0, 1, 1]:
                key_nums.append(4)
            elif result_tmp == [0, 1, 1, 0, 0, 0, 1]:
                key_nums.append(5)
            elif result_tmp == [0, 1, 0, 1, 1, 1, 1]:
                key_nums.append(6)
            elif result_tmp == [0, 1, 1, 1, 0, 1, 1]:
                key_nums.append(7)
            elif result_tmp == [0, 1, 1, 0, 1, 1, 1]:
                key_nums.append(8)
            elif result_tmp == [0, 0, 0, 1, 0, 1, 1]:
                key_nums.append(9)
            else:
                key_nums = []
                break
                

        # 홀수, 짝수 자리 계산 및 검증
        if len(key_nums) == 8:
            hol = 0
            jjak = 0
            for i in range(8):
                if (i + 1) % 2 == 0:
                    jjak += key_nums[i]
                else:
                    hol += key_nums[i]

            if ((hol * 3) + jjak) % 10 == 0:
                total_sum = hol + jjak
                break
            else:
                total_sum = 0
        
    print(f'#{tc} {total_sum}')