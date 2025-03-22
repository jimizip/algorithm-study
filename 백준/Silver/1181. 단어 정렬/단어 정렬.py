import sys
input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
    arr.append(input().strip())

words = list(set(arr))
words.sort()
words.sort(key=len)

for i in words:
    print(i)