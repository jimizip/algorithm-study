T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    result = ''
    print(f'#{tc}')
    for i in range(N):
        C, K = input().split()
        result += (C*int(K))
    
    for i in range(len(result)//10+1):
        print(result[:10])
        result = result[10:]