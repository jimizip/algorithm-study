import sys
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]
result = [0] * (N+1)

# 입력, 데이터 저장
for _ in range(1, N):
    n1, n2 = map(int, input().split())
    # 양방향 저장
    tree[n1].append(n2)
    tree[n2].append(n1)

def DFS(tree, num):
    stack = [num]
    while stack:
        top = stack.pop()
        for i in tree[top]:
            if result[i] == 0:
                result[i] = top
                stack.append(i)
    return result

DFS(tree, 1)

for i in range(2, N+1):
    print(result[i])