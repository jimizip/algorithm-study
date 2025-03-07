T = int(input())
for _ in range(T):
    strVps = input()
    if len(strVps) % 2 == 1:
        print("NO")
    else:
        cnt_l = 0
        cnt_r = 0
        for i in strVps:
            if i == '(':
                cnt_l += 1
            else:
                cnt_r += 1
            if cnt_r > cnt_l:
                print("NO")
                break
        else:
            if cnt_l == cnt_r:
                print("YES")
            else:
                print("NO")