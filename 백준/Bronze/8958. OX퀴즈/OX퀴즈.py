T = int(input())
for _ in range(T):
    result = 0
    score = list(input())
    
    i = 0
    tmp = 0
    while True:
        if score[i] == "O":
            tmp += 1
            result += tmp
            i += 1
            if i >= len(score):
                break
        elif score[i] == "X":
            if len(score) <= (tmp + 1):
                break
            else:
                score = score[i+1:]
                i = 0
                tmp = 0
    
    print(result)