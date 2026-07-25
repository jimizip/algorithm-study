def solution(numbers, target):
    n = len(numbers)
    answer = 0                         

    def dfs(idx, acc):
        nonlocal answer                

        if idx == n:
            if acc == target:     
                answer += 1
            return                   

        dfs(idx + 1, acc + numbers[idx])   
        dfs(idx + 1, acc - numbers[idx])   

    dfs(0, 0)                         
    return answer