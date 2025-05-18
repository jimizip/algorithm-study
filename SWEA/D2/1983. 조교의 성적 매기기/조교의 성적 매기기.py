T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    sli = N // 10
    score = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
    stu = []
    stu_sort = []
    for i in range(N):
        mid, final, task = map(int, input().split())
        stu.append((mid*0.35)+(final*0.45)+(task*0.2))
    stu_sort = sorted(stu, reverse=True)
    
    tmp = (stu_sort.index((stu[K-1])))

    print(f'#{tc} {score[tmp//sli]}')