T = int(input())
for tc in range(1, T + 1):
    fh, fm, lh, lm = map(int, input().split())
    rh = fh + lh
    rm = fm + lm
    if rm > 59:
        rm -= 60
        rh += 1
    if rh > 12:
        rh -= 12
    print(f'#{tc} {rh} {rm}')