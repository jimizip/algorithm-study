T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    result = []
    min_num = min(N, M)

    for i in range(abs(N-M)+1):
        tmp = 0
        for j in range(min_num):
            if len(A) == min_num:
                tmp += (A[j]*B[j+i])
            else:
                tmp += (A[j+i]*B[j])
        result.append(tmp)
    
    print(f'#{tc} {max(result)}')