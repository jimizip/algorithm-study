T = int(input())
for tc in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())
    price_A = 0
    price_B = 0

    price_A = W*P

    if W > R:
        price_B = (Q+((W-R)*S))
    else:
        price_B = Q 

    print(f'#{tc} {min(price_A, price_B)}')