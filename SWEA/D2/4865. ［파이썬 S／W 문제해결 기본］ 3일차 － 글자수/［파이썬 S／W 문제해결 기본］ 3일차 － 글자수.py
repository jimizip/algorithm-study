T = int(input())
for tc in range(1, T+1):
    str1 = input().strip()
    str2 = input().strip()

    dic_1 = dict()

    for i in str1:
        if i in dic_1:
            dic_1[i] += 1
        else:
            dic_1[i] = 1

    dic_2 = dict()
    for i in str2:
        if i in dic_1:
            if i in dic_2:
                dic_2[i] += 1
            else:
                dic_2[i] = 1

    result = max(dic_2.values())

    print(f'#{tc} {result}')