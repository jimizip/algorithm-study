T = int(input())
for tc in range(1, T+1):
    B, W, X, Y, Z = map(int, input().split())
    
    if B == W:
        A = B * X + W * Y
        B = (B + W) * Z
        result = max(A, B)
    else:
        # 최대 쌍 수 계산 (검은공과 흰공 중 적은 수)
        max_count = min(B, W)
        # 쌍을 모두 일치 + 남은 공 일치
        case1 = (max_count * (X + Y)) + ((B - max_count) * X) + ((W - max_count) * Y)
        # 쌍을 모두 불일치 + 남은 공 일치
        case2 = (max_count * 2 * Z) + ((B - max_count) * X) + ((W - max_count) * Y)
        
        result = max(case1, case2)
    
    print(f'{result}')