N, J, H = map(int, input().split())
cnt = 0

while J != H:
    J = (J+1) // 2
    H = (H+1) // 2
    cnt += 1

print(cnt)