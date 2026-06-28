def solution(brown, yellow):
    answer = []
    
    i = 1
    while (True):
        if (yellow % i == 0): # 직사각형
            if (brown == (yellow // i * 2) + (i * 2) + 4):
                answer.append(yellow // i + 2)
                answer.append(i + 2)
                break
        i += 1
        
    return answer