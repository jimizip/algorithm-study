N = int(input())
N_list = list(map(int, input().split()))
N_list.sort()

M = int(input())
M_list = list(map(int, input().split()))

for i in M_list:
    s = 0
    l = N-1
    isTrue = False

    while s <= l:
        mid = (l+s) // 2
        if i == N_list[mid]:
            isTrue = True
            print(1)
            break
        elif i > N_list[mid]:
            s = mid + 1
        else:
            l = mid - 1
    
    if not isTrue:
        print(0)