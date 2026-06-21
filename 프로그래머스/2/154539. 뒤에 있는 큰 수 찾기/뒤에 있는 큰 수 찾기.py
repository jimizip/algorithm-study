def solution(numbers):
    answer = [-1]*len(numbers)
    stack = []
    
    for i in range(len(numbers)):
    
        tmp = numbers[i]
        
        while stack and numbers[stack[-1]] < tmp:
            answer[stack.pop()] = tmp
            
        stack.append(i)
                
    return answer