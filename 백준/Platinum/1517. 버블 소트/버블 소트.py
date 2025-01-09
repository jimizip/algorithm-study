import sys
input = sys.stdin.readline

def merge_sort(s, e):
    global result
    if (e-s) < 1: return
    m = int(s+(e-s) / 2)
    merge_sort(s, m)
    merge_sort(m+1, e)
    for i in range(s, e+1):
        temp[i] = A[i]
    
    k = s
    idx1 = s
    idx2 = m+1
    while idx1 <= m and idx2 <= e:
        if temp[idx1] > temp[idx2]:
            A[k] = temp[idx2]
            result = result + idx2 - k
            idx2 += 1
            k += 1
        else:
            A[k] = temp[idx1]
            idx1 += 1
            k += 1
    while idx1 <= m:
        A[k] = temp[idx1]
        idx1 += 1
        k += 1
    while idx2 <= e:
        A[k] = temp[idx2]
        idx2 += 1
        k += 1


# 입력
N = int(input())
A = list(map(int, input().split()))
temp = [0] * int(N+1)
result = 0

A.insert(0, 0)
merge_sort(1, N)

# 출력
print(result)