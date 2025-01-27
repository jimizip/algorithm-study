# 입력
n = int(input())

# 초기화
fi = [0, 1]

for i in range(2, n+1):
    fi.append(fi[i-1]+fi[i-2])

# 출력
print(fi[n])