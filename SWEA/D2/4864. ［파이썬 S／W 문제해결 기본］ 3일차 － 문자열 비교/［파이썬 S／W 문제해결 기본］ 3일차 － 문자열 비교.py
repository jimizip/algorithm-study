T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    result = 0

    while len(str2) >= len(str1):
        if str1[0] in str2:
            first = str2.index(str1[0])
            tmp = str2[first:first+len(str1)]

            if tmp == str1:
                result = 1
                break
            else:
                str2 = str2[first+1:]
        else:
            result = 0
            break


    print(f'#{tc} {result}')