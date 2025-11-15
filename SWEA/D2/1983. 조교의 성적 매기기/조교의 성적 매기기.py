T = int(input())
grade_table = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for t in range(1, T+1):
    N, K = map(int, input().split())
    stu_arr = []
    for _ in range(N):
        m, f, a = map(int, input().split())
        avg = m*0.35 + f*0.45 + a*0.2
        stu_arr.append(avg)
    rank = sorted(stu_arr, reverse=True)
    k_score = stu_arr[K-1]
    k_index = rank.index(k_score)
    grade_idx = k_index * 10 // N   # N명이면 10개로 나눔
    print(f'#{t} {grade_table[grade_idx]}')