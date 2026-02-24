N = int(input())
arr = list(map(int, input().split()))
result = [0]*len(arr)
stack = []

for i in range(len(arr)-1, -1, -1):
    while stack and arr[i] >= arr[stack[-1]]:
        result[stack[-1]] = i+1
        stack.pop()
    stack.append(i)

print(' '.join(map(str, result)))