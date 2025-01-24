# 입력
T = int(input())

fib = [[1, 0], [0, 1]]  # [0의 출력 횟수, 1의 출력 횟수]

for i in range(2, 41):
    fib.append([fib[i-1][0] + fib[i-2][0], fib[i-1][1] + fib[i-2][1]])

# 출력
for _ in range(T):
    N = int(input())
    print(fib[N][0], fib[N][1])