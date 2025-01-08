# 입력
N = int(input())
ans = [0] * N
A = list(map(int, input().split()))
myStack = []
result = ""

# 스택이 값이 있고 지금 들어오는 값이 스택에 있는 인덱스의 값보다 크면 정답 배열에 지금 값 저장
for i in range(N):
    while myStack and A[myStack[-1]] < A[i]:
        ans[myStack.pop()] = A[i]
    myStack.append(i)

# 마지막 수는 -1
while myStack:
    ans[myStack.pop()] = -1

# 출력
print(" ".join(list(map(str, ans))))