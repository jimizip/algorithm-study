T = int(input())
for tc in range(1, 1+T):
    arr = list(map(int, input().split()))
    h = arr[0] + arr[2]
    m = arr[1] + arr[3]

    if h > 12:
        h -= 12
    
    if m > 59:
        h += (m//60)
        m = m - 60
    
    print(f'#{tc} {h} {m}')