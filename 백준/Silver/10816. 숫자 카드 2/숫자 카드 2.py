from collections import Counter
import sys
input = sys.stdin.readline
N = int(input())

num_list = list(map(int, input().split()))

counter = Counter(num_list)

M = int(input())
result_num = list(map(int, input().split()))

for i in result_num:
    if i in counter:
        print(counter[i], end = ' ')
    else:
        print(0, end = ' ')