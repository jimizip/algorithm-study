N = input()
if len(N) < 2:
        N = '0' + N
cnt = 1

def sol(N):
    tmp = str(int(N[0]) + int(N[1]))
    if len(tmp) < 2:
        tmp = '0' + tmp
    N = N[1] + tmp[1]
    return N

result = ''
result = sol(N)
while N != result:
    cnt += 1
    result = sol(result)

print(cnt)