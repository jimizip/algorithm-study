import sys
from collections import deque

input = sys.stdin.readline

# 입력
N, L = map(int, input().split())
A = list(map(int, input().split()))

mydeque = deque()

for i in range(N):
    # 1. 뒤에서 부터 비교하여 삭제 (데이터 값)
    while mydeque and mydeque[-1][0] > A[i]:
        mydeque.pop()
    # 덱에 작은 값 넣어주기
    mydeque.append((A[i], i))

    # 2. 앞에 비교해서 슬라이딩 값 넘어가면 삭제 (인덱스)
    if mydeque[0][1] <= i-L:
        mydeque.popleft()

    # 출력
    print(mydeque[0][0], end=' ')
